from django.shortcuts import render, redirect, reverse
from django.http import Http404, JsonResponse

from book.models import Book
import random


# Create your views here.


def index(request):
    economy = []
    for book in Book.objects.filter(kind_id=1):
        economy.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                        "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(economy)

    fiction = []
    for book in Book.objects.filter(kind_id=2):
        fiction.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                        "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(fiction)

    science = []
    for book in Book.objects.filter(kind_id=3):
        science.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                        "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(science)

    life = []
    for book in Book.objects.filter(kind_id=4):
        life.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                     "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(life)

    literature = []
    for book in Book.objects.filter(kind_id=5):
        literature.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                           "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(literature)

    recommend = []
    for book in Book.objects.filter(kind_id=5):
        recommend.append({"id": book.book_id, "picture": "static/" + book.book_picture,
                          "url": "book/detail/" + str(book.book_id) + "/"})
    random.shuffle(recommend)
    return render(request, 'index.html', {"economy": economy[0:5], "fiction": fiction[0:5], "science": science[0:5],
                                          "life": life[0:5], "literature": literature[0:5],
                                          "recommend": recommend[0:5]})


def login_needful(func):
    def in_fun(request):
        if request.session.get('islogin', False):
            return func(request)
        else:
            return redirect(reverse('user:login'))

    return in_fun


def login_needful_json_res_0_errmsg(func):
    def in_fun(request):
        if request.session.get('islogin', False):
            return func(request)
        else:
            return JsonResponse({'res': 0, 'errmsg': '未登录'})

    return in_fun
