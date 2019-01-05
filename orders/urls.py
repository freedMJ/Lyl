from django.conf.urls import  url
from orders import views
from orders.views import IndexView,ResultView,Result_usertokenView,Result_ordernoView,Is_filledView,LoginView



urlpatterns = [

    #url(r'^index',views.index),
    url(r'^index',IndexView.as_view(),name='index'),#首页
    #url(r'^result_time(?P<pindex>\d*)$',views.result),
    url(r'^result_time(?P<pindex>\d*)$',ResultView.as_view(),name='result_time'),#根据时间段查询
    #url(r'^result_usertoken(?P<pindex>\d*)$',views.result_usertoken),
    url(r'^result_usertoken(?P<pindex>\d*)$',Result_usertokenView.as_view(),name='result_usertoken'),#根据用户标识查询
    #url(r'^result_orderno$',views.result_orderno),
    url(r'^result_orderno$',Result_ordernoView.as_view(),name='result_orderno'),#根据订单号查询
    #url(r'^is_filled$',views.is_filled),
    url(r'^is_filled$',Is_filledView.as_view(),name='is_filled'),#查询是否分发成功
    url(r'^register',views.register),
    #url(r'^login',views.login),
    url(r'^',LoginView.as_view(),name='login'),
]