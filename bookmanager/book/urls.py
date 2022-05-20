# 为了方便路由的管理，建议在每个子应用中建立urls
from django.urls import path

from book.views import index

urlpatterns = [
    path('index/', index)
]

