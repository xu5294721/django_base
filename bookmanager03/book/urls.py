from django.urls import path
from book.views import create_book, req_url, req_query, shop_02, register

urlpatterns = [
    path('create/', create_book),
    path('<city_id>/<shop_id>/', req_url),
    path('req_query/', req_query),
    path('shop02/', shop_02),
    path('register/', register),

]
