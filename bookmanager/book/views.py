from django.shortcuts import render, HttpResponse


# Create your views here.
# 视图实际上就是python函数
# 1.视图函数第一个参数是请求，实际上就是HttpRequest
# 2.必须返回一个响应

def index(request):

    return HttpResponse('欢迎')
