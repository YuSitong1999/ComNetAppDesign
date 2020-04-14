import io

from django.forms import model_to_dict
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from book.models import Book
from user.models import Cart
from order.models import Order, OrderContent
from django.core import serializers
from bookstore import settings

import datetime

from alipay import AliPay  # https://blog.csdn.net/appleyuchi/article/details/104613313
import qrcode, time
import urllib


def all(request):
    user_id = request.session['user']['user_id']
    # all_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=[s for s in range(0,5)])]
    cancel_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=0)]
    unpaid_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=1)]
    unsent_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=2)]
    unreceived_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=3)]
    finished_list = [model_to_dict(order) for order in Order.objects.filter(user_id=user_id, status=4)]
    content = {
        'cancel_list': cancel_list,
        'unpaid_list': unpaid_list,
        'unsent_list': unsent_list,
        'unreceived_list': unreceived_list,
        'finished_list': finished_list,
        # 'all_list': all_list
    }
    # 因为没有对应前端，先返回成json
    return render(request, 'order/all.html', content)


def detail(request, order_id):
    content = {}
    # 订单本身的信息
    try:
        order = Order.objects.get(order_id=order_id)
    except Cart.DoesNotExist:
        return Http404
    except Cart.MultipleObjectsReturned:
        raise Exception('同一订单号出现多次')

    # object 转 dict
    content['order'] = model_to_dict(order)
    # 计算总付款数=总价+运费
    content['order']['all_price'] = content['order']['sum_price'] + 10

    # 订单中书籍的信息
    content['order_content'] = []
    order_content = OrderContent.objects.filter(order_id=order_id)
    for book in order_content:
        element = {
            'id': book.order_id,
            'book_id': book.book_id,
            'number': book.number,
            'price': book.price * book.number,  # 小计：可能不只一本同种书的总价
        }
        try:
            book = Book.objects.get(book_id=book.book_id)
        except Cart.DoesNotExist:
            raise Exception('书编号%d不存在' % book.book_id)
        except Cart.MultipleObjectsReturned:
            raise Exception('书编号%d出现多次' % book.book_id)
        element.update({
            'book_name': book.book_name,
            'book_picture': book.book_picture,
            'book_price': book.price,
            'author': book.author,
            'press': book.press,
            'kind_name': book.kind_name,
        })
        content['order_content'].append(element)
    return render(request, 'order/detail.html', content)


# 创建订单
def new(request):
    order = Order(
        # order_id =
        user_id=request.session['user']['user_id'],
        sum_price=0,
        # 订单状态：已取消 0， 待付款 1， 待发货 2， 已发货 3， 已完成 4
        status=1,
        time_submit=datetime.datetime.now(),
        # time_pay=None,
        # time_finish=None,
    )
    order.save()

    # print(order.order_id)

    sum_price = 0.0
    for book in Cart.objects.filter(
            user_id=request.session['user']['user_id'],
            select=True,
    ).all():
        OrderContent.objects.create(
            order_id=order.order_id,
            book_id=book.book_id,
            number=book.number,
            price=book.price
        )
        sum_price += book.number * book.price
    Order.objects.filter(order_id=order.order_id).update(sum_price=sum_price)
    Cart.objects.filter(
        user_id=request.session['user']['user_id'],
        select=True,
    ).delete()
    # order.save()
    # return JsonResponse({'res': 1, 'order_id':order.order_id})
    return detail(request, order.order_id)


def receive(request):
    try:
        order_id = int(request.GET.get('order_id'))
    except ValueError:
        return JsonResponse({'res': 0, 'errmsg': '订单号错误'})
    try:
        order = Order.objects.get(user_id=request.session['user']['user_id'], order_id=order_id)
    except Order.DoesNotExist:
        # 订单不存在
        return JsonResponse({'res': 0, 'errmsg': '订单不存在'})
    except Order.MultipleObjectsReturned:
        raise Exception('订单表错误')
    if order.status == 3:
        order.status = 4
        order.save()
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0, 'errmsg': '订单不可收货'})


alipayClient = AliPay(
    appid=settings.APP_ID,
    app_notify_url=None,
    app_private_key_string=settings.APP_PRIVATE_KEY,
    alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY,
    sign_type='RSA2',
    debug=settings.DEBUG,
)


def alipay_pay(request):
    global alipayClient

    out_trade_no = request.GET.get('order_id')  # 555 开始
    if out_trade_no is None:
        print('无order_id')
        return
    try:
        order_id = int(out_trade_no)
    except ValueError:
        print('order_id非整数')
        return

    if settings.DEBUG:
        out_trade_no += ('__%s' % datetime.datetime.now()).split('.')[0].replace(' ', '_').replace('-', '_').replace(':', '_')
        print(out_trade_no)
    try:
        order = Order.objects.get(order_id=order_id)
    except Order.DoesNotExist:
        # 订单不存在
        print('order_id 订单不存在')
        return
    except Order.MultipleObjectsReturned:
        raise Exception('订单表错误')

    # 书籍总价加运费
    total_amount = order.sum_price + 10.00
    subject = '珞珈在线书店订单 %s' % order.time_submit
    timeout_express = '30m'
    try:
        dict = alipayClient.api_alipay_trade_precreate(out_trade_no=out_trade_no, total_amount=total_amount,
                                                       subject=subject, timeout_express=timeout_express)
    except urllib.error.URLError:
        raise Exception('网络已断开')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(dict['qr_code'])  # 从URL获取二维码所含信息
    img = qr.make_image()  # 生成二维码图片
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    img.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
