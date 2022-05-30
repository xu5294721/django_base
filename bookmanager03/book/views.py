from django.shortcuts import render, HttpResponse

# Create your views here.
from book.models import BookInfo, PeopleInfo


def create_book(request):
    return HttpResponse('create')


def shop(request, city_id, shop_id):
    return HttpResponse('君的饭店')
