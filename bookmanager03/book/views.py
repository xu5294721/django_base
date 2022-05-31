from django.shortcuts import render, HttpResponse

# Create your views here.
from book.models import BookInfo, PeopleInfo


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
