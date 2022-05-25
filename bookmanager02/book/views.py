from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('index')


# objects--相当一个代理  实现增删改查
from book.models import BookInfo

BookInfo.objects.create(
    name='测试开发简介',
    pub_date='2010-01-01',
    readcount=20,
)
