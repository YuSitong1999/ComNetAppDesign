

# ComNetAppDesign

### 计算机网络应用设计实验——网上书店



#### 老师要求

> 应用程序要求实现一个网上书店的基本功能，要求具有前端（用户）和后端（管理）功能，基于Web运行方式。前端具有浏览书目、购物车等功能，后端具有管理书目、基本统计功能。
>
> - 客户端操作系统为Windows



#### 开发环境

- 前端框架：Bootstrap
- 前端开发语言：HTML5   CSS    JavaScript
- 后端框架：Django
- 后端开发语言：Python



#### 数据库

*用户APP*

> | 用户信息表 |               |
> | ---------- | ------------- |
> | 用户号     | user_id       |
> | 用户名     | user_name     |
> | 密码       | password      |
> | 电话       | phone_number  |
> | 地址       | address       |
> | 电子邮件   | email         |
> | 注册日期   | register_date |
>
> 
>
> | 购物车表     |         |
> | ------------ | ------- |
> | 用户号       | user_id |
> | 购物车书籍号 | book_id |
> | 书籍数量     | number  |
> | 书籍单价     | price   |



*书籍APP*

> | 书籍信息表           |              |
> | -------------------- | ------------ |
> | 书籍号               | book_id      |
> | 书名                 | name         |
> | 书籍图片URL          | book_picture |
> | 书籍价格             | price        |
> | 书籍原价             | price_old    |
> | 作者                 | author       |
> | ISBN                 | isbn         |
> | 出版社               | press        |
> | 库存（书本剩余数量） | rest         |
> | 类别号               | kind_id      |
> | 类别名               | kind_name    |
> | 内容简介             | description  |
> | 销量                 | sales        |



*订单APP*

> | 订单表       |             |
> | ------------ | ----------- |
> | 订单号       | order_id    |
> | 用户号       | user_id     |
> | 订单总价     | sum_price   |
> | 订单状态     | status      |
> | 订单提交时间 | time_submit |
> | 订单付款时间 | time_pay    |
> | 订单完成时间 | time_finish |
>
>  
>
> | 订单内容表 |          |
> | ---------- | -------- |
> | 订单号     | order_id |
> | 订单书籍号 | book_id  |
> | 书籍数量   | number   |
> | 书籍单价   | price    |



#### 网页URL

> | 主页                                         | index/                             | 说明（页面按前端描述，接口按后端描述）                       |
> | -------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
> | 用户相关页面                                 | user/...                           |                                                              |
> | 书籍相关页面                                 | book/...                           |                                                              |
> | 订单相关页面                                 | order/...                          |                                                              |
> | 后台相关页面                                 | admin/...                          |                                                              |
> | 主页                                         | （空）                             |                                                              |
> |                                              |                                    |                                                              |
> | 登录页                                       | user/login                         | 输入登录信息，调用登录验证接口，若返回成功，跳转到主页       |
> | 我的主页（可更改个人信息，提交生效）         | user/detail                        | 可以直接更新信息，需要输入原密码，点击提交调用提交个人信息更新接口，返回成功则刷新，失败显示提示 |
> | 注册页                                       | user/register                      | 输入注册信息，调用注册验证接口，若返回成功，跳转到注册成功页 |
> | 注册成功页（自动跳转到主页）                 | user/result                        | 显示注册成功信息，几秒种后跳转到主页                         |
> | 购物车页                                     | user/cart                          | 显示购物车书籍基本信息，点击查看书籍详细信息，支持移出购物车，点击提交 |
> | 确认订单页面（暂不实现：选择收货地址电话等） | user/order                         | 显示购物车书籍基本信息，计算总价，点击确认调用创建新订单接口，成功跳转到我的订单页面 |
> |                                              |                                    |                                                              |
> | 登出接口                                     | user/logout                        | 删除session中的登录信息                                      |
> | 验证码接口                                   | user/verifycode                    | 返回验证码图片                                               |
> | 验证邮箱接口                                 | user/verifyemail                   | 验证邮箱地址格式，发送邮件，返回是否成功，不成功返回错误信息 |
> | 注册验证接口                                 | user/register_check                | 验证注册信息，返回是否符合要求，不符合要求返回错误信息       |
> | 登录验证接口                                 | user/login_check                   | 验证登录信息，返回是否符合要求，不符合要求返回错误信息       |
> | 提交个人信息更新接口                         | user/update                        | 验证新个人信息，返回是否符合要求，不符合要求返回错误信息     |
> |                                              |                                    |                                                              |
> | 我的订单页面                                 | order/all                          | 分为待支付、待发货、待收货、已完成展示订单基本信息           |
> | 订单详情页面                                 | order/detail?order_id=\<order_id>  | 显示订单详细信息                                             |
> |                                              |                                    |                                                              |
> | （以购物车中的所有商品）创建新订单接口       | order/new                          | 创建新的待支付订单，清空购物车                               |
> | （订单状态待收货改为）已收货接口             | order/receive?order_id=\<order_id> | 订单状态从待收货改为已完成                                   |
> |                                              |                                    |                                                              |
> | 某类书籍页面                                 | book/kind?kind_id=\<int:kind_id>   | 显示此类书籍基本信息，点击跳转到详细信息                     |
> | 书籍详情页面                                 | book/detail?book_id=\<int:book_id> | 显示此书籍详细信息，点击加入购物车调用相应接口               |
> | 搜索书籍结果页面                             | book/search?q=\<str:q>             | 显示搜索到的书籍基本信息，点击跳转到详细信息                 |
> |                                              |                                    |                                                              |
> | 加入购物车接口                               | book/buy?book_id=\<int:book_id>    | 购物车表没有加入，已有数量+1                                 |
> | 移出购物车接口                               | book/cancel?book_id=\<int:book_id> | 移出购物车表                                                 |
>

#### 主要流程

点击加入购物车：①调用加入购物车接口②显示加车成功/失败提示

购物车页面 点击移出购物车：①调用移出购物车接口②显示加车成功/失败提示

**下单**

查看购物车：返回页面包含购物车中的书籍信息

点击提交：进入确认订单页面

点击确认：①调用创建新订单接口，若成功②跳转到我的订单页面

凭订单号加客服微信支付，后台改成待发货

发货后，后台改成待收货

我的订单页面，点击收货：①调用已收货接口②刷新页面，更新订单状态



#### 任务完成统计表

P.s. 日期就某一时间段/教学周，干了啥每个人记录一下，怕忘掉orz

*武涵*

> | 日期 | 任务 |
> | ---- | ---- |
> |      |      |
> |      |      |
> |      |      |



*张真*

> | 日期 | 任务 |
> | ---- | ---- |
> |      |      |
> |      |      |
> |      |      |



*于斯同*

> | 日期 | 任务 |
> | ---- | ---- |
> |      |      |
> |      |      |
> |      |      |



*骆雅婧*

> | 日期 | 任务 |
> | ---- | ---- |
> |      |      |
> |      |      |
> |      |      |