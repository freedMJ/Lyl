from django.conf.urls import include,url
#from . import views
from orders.views import IndexView,ResultView,Result_usertokenView,Result_ordernoView,Is_filledView,LoginView,TestViews



urlpatterns = [

    url(r'^index',IndexView.as_view(),name='index'),#首页
    url(r'^result_time(?P<pindex>\d*)$',ResultView.as_view(),name='result_time'),#根据时间段查询
    url(r'^result_usertoken(?P<pindex>\d*)$',Result_usertokenView.as_view(),name='result_usertoken'),#根据用户标识查询
    url(r'^result_orderno$',Result_ordernoView.as_view(),name='result_orderno'),#根据订单号查询
    url(r'^is_filled(?P<pindex>\d*)$',Is_filledView.as_view(),name='is_filled'),#查询是否分发成功
    url(r"^test(?P<pindex>\d*)$",TestViews.as_view()),
    url(r'^',LoginView.as_view(),name='login'),
]