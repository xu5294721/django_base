from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect

# Create your views here.
from django.views import View


def create_book(request):
    return HttpResponse('create')


# HttpRequset对象：
# 1.URL方式  截取URL特定部分，在服务器端的路由中用正则表达式截取。用于接收参数，向服务器传递数据
def req_url(request, city_id, shop_id):
    # 查询字符串方式获取
    # query_params = request.GET
    # print(query_params)
    # order = query_params.getlist('order')
    # print(order)
    return HttpResponse('君的饭店')


# 2.查询字符串(query_string),例如/?key1=value&key2=values2
def req_query(request):
    query_params = request.GET
    print(query_params)
    order = query_params.getlist('order')
    for i in order:
        print(i)

    return HttpResponse('req_query')


def shop_02(request):
    req_params = request.GET
    order = req_params.get('id')
    print(order)
    return HttpResponse('shop_02')


# 3.传递POST请求，
def register(request):
    req_post = request.POST
    print(req_post)
    return HttpResponse('register')


# 4.传递JSON数据
def json(request):
    json_body = request.body
    # 转换为字符串形式
    body_str = json_body.decode()
    print(body_str)
    # 将字符串转换为python字典格式
    # body_dict = json.loads(body_str)
    # print(body_dict)

    #   5.请求头
    print(request.META['SERVER_PORT'])

    return HttpResponse('JSON')


# method 查看请求的方式 GET OR POST
def method(request):
    print(request.method)

    return HttpResponse('method')


# ##############Response响应头##################
def response(request):
    # res = HttpResponse('res11', status=201)
    # res['name'] = 'keyone'

    # 将JSON数据发送出去 ， Response处理.
    # 利用JsonResponse 把字典转换为JSON数据
    info = [
        {
            "name": "keyone",
            "address": "nanchang",
        },
        {
            "name": "keyone",
            "address": "yingtan",
        }
    ]
    from django.http import JsonResponse
    res = JsonResponse(data=info, safe=False)
    return res


# 重定向
def redir(request):
    return redirect('https://www.baidu.com')


##############################################################
# cookie 是保存在浏览器中的数据

# 服务器端设置cookie
def set_cookie(request):
    # 1.获取查询字符串数据
    username = request.GET.get('username')
    # 2.服务器端设置cookie
    # 通过响应对象set_cookie
    response1 = HttpResponse('set_cookie')
    response1.set_cookie('name', username, max_age=24 * 60 * 60)

    # 删除cookie
    # response1.delete_cookie('name')

    return response1


# 获得cookie
def get_cookie(request):
    # request.COOKIES获取cookie，为字典数据   表现为键值对形式
    name = request.COOKIES.get('name')
    return HttpResponse(name)


#########################################################
# session 是保存在服务器端,数据相对安全
# session 需要依赖于cookie

# 设置session
def set_session(request):
    username = request.GET.get('username')
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    return HttpResponse('set_session')


# 获取session
def get_session(request):
    username = request.session.get('username')
    user_id = request.session.get('user_id')
    # 格式化数据，输出session
    content = '{},{}'.format(user_id, username)

    return HttpResponse(content)


"""
类视图的定义  继承View
    用于一个视图内，实现多个请求方法。
class 类试图名(View):
    def get():
        return
    def post():
        return

1.继承自View
2.类视图中的方法，采用http方法小写来区分不同的请求
"""


class LoginView(View):
    # self 为对象方法
    def get(self, request):
        return HttpResponse('get get get ')

    def post(self, request):
        return HttpResponse('post post post')


"""

定义一个订单/个人中心   类视图
如果登录成功，则跳转订单页面
如果没有登录，则跳转到未登录页面。

判断如果没有登录，跳转不同view

"""


# LoginRequiredMixin：用于 内部会自动判断用户是否登录的判断（以admin站点）：
#   如果登录成功，则显示页面； 没成功，则系统会自动为跳转至系统的accounts/login/  页面中去
# 是Django中内置类
#
# 多继承，mro调用顺序为： 先LoginRequiredMixin 后调用View
class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('Get 登录成功，正在订单页面')
