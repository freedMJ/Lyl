from django.conf.urls import include,url
from . import views
from orders.views import ResultView,LoginView,LoadView,index



urlpatterns = [

   	url(r'^index$',views.index,name='index'),#首页
   	url(r'^result_load(?P<pindex>\d*)$',LoadView.as_view(),name='result_load'),#根据时间段查询
    url(r'^result_time(?P<pindex>\d*)$',ResultView.as_view(),name='result_time'),#根据时间段查询
    url(r'^',LoginView.as_view(),name='login'),
]



