from django.urls import path
from book.views import create_book, req_url, req_query, shop_02, register, json, method

urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<int:shop_id>/', req_url),
    path('req_query/', req_query),
    path('shop02/', shop_02),
    path('register/', register),
    path('json/', json),
    path('method/', method)

]
