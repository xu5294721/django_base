from django.urls import path
from book.views import create_book, req_url, req_query, shop_02, register, json, method, response, redir, \
    set_cookie, get_cookie, set_session, get_session, LoginView, OrderView

urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<int:shop_id>/', req_url),
    path('req_query/', req_query),
    path('shop02/', shop_02),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/', response),
    path('redir/', redir),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),

    ########类视图中的方法调用###############
    path('163login/', LoginView.as_view()),
    path('order/', OrderView.as_view()),
]
