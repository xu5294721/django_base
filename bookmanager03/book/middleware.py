# 中间件   要在setting.py中注册
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):
    # 请求中间件
    def process_request(self, request):
        print('每次请求前，都会调用执行process_request')
        username = request.COOKIES.get('name')
        if username is None:
            print('没有得到用户信息')
        else:
            print('获取了用户信息')

    # 响应中间件
    def process_response(self, request, response):
        print('每次响应前，都会调用执行process_response')
        return response
