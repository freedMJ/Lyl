from django.conf.urls import include,url
from . import views
from orders.views import ResultView,LoginView,index



urlpatterns = [

   	url(r'^index$',views.index,name='index'),#首页
    url(r'^result_time(?P<pindex>\d*)$',ResultView.as_view(),name='result_time'),#多条件查询
    url(r'^',LoginView.as_view(),name='login'),
]



