from django.shortcuts import HttpResponse, redirect


# Create your views here.


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
