from django.shortcuts import render,redirect
from orders.models import Orders
from django.http import HttpResponse,HttpResponseRedirect
import time
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.db.models import Count
from django.core.paginator import Paginator
from django.views.generic import View,ListView
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from utils.mini import LoginRequiredMini
import math
from django.views.generic import ListView
from django.views import generic
from utils import constants,get_page
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django_redis import get_redis_connection
from django.conf import settings
from django.core.cache import cache



# Create your views here.
#查询某一段时间的订单	
class ResultView(LoginRequiredMini,View):
	def get(self,request,pindex):
		#从redis数据库中
		key_str=request.COOKIES.get('result_key')
		if not key_str:
			key_str='nokey'
		flage=cache.has_key(key_str)		
		print(flage)
		if flage:	
			try:
				olist=cache.get(key_str)
			except Exception as e:
				return HttpResponse("数据查询失败")

		else:
			orderMethod=request.GET.get('orderMethod')
			start_time_stamp=request.GET.get("start_timestamp")
			end_time_stamp=request.GET.get("end_timestamp")
			usertoken=request.GET.get("usertoken")#	用户标识 选填
			orderno=request.GET.get("orderno")#订单号 选填
			orderType=request.GET.get("orderType")#订单种类 必填
			isfilled=request.GET.get("isfilled")#是否已分发 必填
			if orderno=="0" and orderType!='3':
				try:
					if not all([start_time_stamp,end_time_stamp]):
						return HttpResponse("开始时间与结束时间必填")
					start_timestamp=int(start_time_stamp)
					end_time_stamp=int(end_time_stamp)
					olist=Orders.objects.filter(created_at__gt=start_time_stamp,created_at__lt=end_time_stamp)
					if usertoken!='0':
						olist=olist.filter(usertoken='%s'%usertoken)
					if orderType=='2':
						olist=olist.filter(orderno__contains='LYL2')
					if orderType=='3':
						olist=olist.filter(orderno__contains='LYLGD')
					if orderno!='0':
						olist=olist.filter(orderno='%s'%orderno)
					if isfilled=='0':
						olist=olist.filter(is_filled=0)
					if isfilled=='1':
						olist=olist.filter(is_filled=1)
						print(olist)
					print("xxxxxxxxxxx")
				except Exception as e:
					return HttpResponse("数据查询错误")
			if orderno!="0":
				try:
					olist=Orders.objects.filter(orderno='%s'%orderno)
				except Exception as e:
					return HttpResponse("数据查询错误")
			"""
			if orderno!='0':
				print("aaa")
				try:
					olist=Orders.objects.get(orderno='%s'%orderno)
					print(olist)
				except Exception as e:
					return HttpResponse("数据查询错误")

			"""
			print("55555555555")
			print(type(orderMethod))
			print(orderno)
			print(olist)
			try:
				#将得到的结果存进redis数据库中
				cache.set(key_str,olist,60*60)
				print("ffffff")
			except Exception as e:
				return HttpResponse("数据保存失败")
		#分页
		olength=len(olist)
		paginator=Paginator(olist,constants.HTML_PAGE_NUMS) #每页5条
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		page=paginator.page(pindex)
		total_page_number=paginator.num_pages
		len_pindex=math.ceil(float(olength/constants.HTML_PAGE_NUMS))
		page_list=get_page.get_pages(int(total_page_number),int(pindex))
		if pindex>1:
			flage=True
		return render(request,'htmls/template.html',{'page':page,'page_list':page_list,'olength':olength,'len_pindex':len_pindex,'flage':flage})

#登录
class LoginView(View):
	def get(self,request):
		return render(request,'htmls/login.html')

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				next_url=request.GET.get('next',reverse('orders:index'))
				response=redirect(next_url)
				return response
			else:
				return render(request,'htmls/login.html',{'errmsg':'该用户不存在'})
		else:
			return render(request,'htmls/login.html',{'errmsg':'用户名或密码错误'})

#跳转首页
def index(request):
	return render(request,'htmls/result.html')

