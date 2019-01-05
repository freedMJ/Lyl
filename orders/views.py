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
# Create your views here.

#首页
"""def index(request):
	endTime_unix=time.time()
	startTime_unix=time.localtime(endTime_unix-3600)
	startTime=get_time(startTime_unix)
	n_endTime_unix=time.localtime(endTime_unix)
	endTime=get_time(n_endTime_unix)
	errormge1=''#查时间范围输入时间错误
	errormge2=''#查时间范围没输入用户表示
	errormge3=''#查用户没输入时间
	if request.GET.get('message')=='errorTime1':
		errormge1='请输入正确的时间格式'
		return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge1':errormge1})
	elif request.GET.get('message')=='errorNoUsertoken':
		  errormge2='用户标识不能为空'
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
	elif request.GET.get('message')=='errorNoUsertokenTime':
		  errormge2='请输入正确的时间格式'
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
	elif request.GET.get('message')=='errorNoUser':
		  errormge2='该用户不存在或用户标识错误'
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
	elif request.GET.get('message')=='errorNoOrderno':
		  errormge3="订单号不允许为空"
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge3':errormge3})
	elif request.GET.get('message')=='errorOrderno':
		  errormge3="订单号输入错误或订单号不存在"
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge3':errormge3})
	elif request.GET.get('message')=='errorTime2':
		  errormge4="请输入正确的时间格式"
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge4':errormge4})
	elif request.GET.get('message')=='errorOrderno2':
		  errormge4="该段时间没有订单"
		  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge4':errormge4})

	return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge1':errormge1})"""

class IndexView(LoginRequiredMini,View):
	def get(self,request):
		endTime_unix=time.time()
		startTime_unix=time.localtime(endTime_unix-3600)
		startTime=get_time(startTime_unix)
		n_endTime_unix=time.localtime(endTime_unix)
		endTime=get_time(n_endTime_unix)
		errormge1=''#查时间范围输入时间错误
		errormge2=''#查时间范围没输入用户表示
		errormge3=''#查用户没输入时间
		if request.GET.get('message')=='errorTime1':
			errormge1='请输入正确的时间格式'
			return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge1':errormge1})
		elif request.GET.get('message')=='errorNoUsertoken':
			  errormge2='用户标识不能为空'
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
		elif request.GET.get('message')=='errorNoUsertokenTime':
			  errormge2='请输入正确的时间格式'
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
		elif request.GET.get('message')=='errorNoUser':
			  errormge2='该用户不存在或用户标识错误'
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge2':errormge2})
		elif request.GET.get('message')=='errorNoOrderno':
			  errormge3="订单号不允许为空"
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge3':errormge3})
		elif request.GET.get('message')=='errorOrderno':
			  errormge3="订单号输入错误或订单号不存在"
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge3':errormge3})
		elif request.GET.get('message')=='errorTime2':
			  errormge4="请输入正确的时间格式"
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge4':errormge4})
		elif request.GET.get('message')=='errorOrderno2':
			  errormge4="该段时间没有订单"
			  return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge4':errormge4})

		return render(request,'htmls/index.html',{'startTime':startTime,"endTime":endTime,'errormge1':errormge1})

#查询某一段时间的订单
"""def result(request,pindex):
	if request.method =="POST":
		start_time=request.POST['start_time']
		end_time=request.POST['end_time']
		#校验时间是否正确
		try :
			s_timeStamp=get_unix(start_time)
			e_timeStamp=get_unix(end_time)
		except Exception:
			#return render(request,'htmls/index.html',{'errmsg_time':'请输入正确的时间格式','startTime':startTime,"endTime":endTime})
			return HttpResponseRedirect('index/?message=errorTime1')
			#return redirect(reverse('orders.views.index/?message=error'))
		request.session['s_timeStamp']=s_timeStamp
		request.session['e_timeStamp']=e_timeStamp
	if request.method =='GET':
		s_timeStamp=request.session['s_timeStamp']
		e_timeStamp=request.session['e_timeStamp']

	olist=Orders.objects.filter(Q(created_at__gt=s_timeStamp)&Q(created_at__lt=e_timeStamp))
	olength=len(olist)
	#分页
	paginator=Paginator(olist,25)
	if pindex=="":
		pindex=1
	else:
		pindex=int(pindex)
	#第i页实例对象
	page=paginator.page(pindex)

	return render(request,'htmls/result_list.html',{'page':page,'olength':olength})"""
#查询某一段时间的订单
class ResultView(LoginRequiredMini,View):
	def get(self,request,pindex):
		s_timeStamp=request.session['s_timeStamp']
		e_timeStamp=request.session['e_timeStamp']
		olist=Orders.objects.filter(Q(created_at__gt=s_timeStamp)&Q(created_at__lt=e_timeStamp))
		olength=len(olist)
		#分页
		paginator=Paginator(olist,25)
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		#第i页实例对象
		page=paginator.page(pindex)

		return render(request,'htmls/result_list.html',{'page':page,'olength':olength})
	def post(self,request,pindex):
		start_time=request.POST['start_time']
		end_time=request.POST['end_time']
		#校验时间是否正确
		try :
			s_timeStamp=get_unix(start_time)
			e_timeStamp=get_unix(end_time)
		except Exception:
			#return render(request,'htmls/index.html',{'errmsg_time':'请输入正确的时间格式','startTime':startTime,"endTime":endTime})
			return HttpResponseRedirect('index/?message=errorTime1')
			#return redirect(reverse('orders.views.index/?message=error'))
		request.session['s_timeStamp']=s_timeStamp
		request.session['e_timeStamp']=e_timeStamp
		olist=Orders.objects.filter(Q(created_at__gt=s_timeStamp)&Q(created_at__lt=e_timeStamp))
		olength=len(olist)
		#分页
		paginator=Paginator(olist,25)
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		#第i页实例对象
		page=paginator.page(pindex)

		return render(request,'htmls/result_list.html',{'page':page,'olength':olength})



#根据用户标识查询某一范围时间的订单详情
"""
def result_usertoken(request,pindex):
	if request.method=='POST':
		ausertoken=request.POST['ausertoken']
		if not ausertoken:
			return HttpResponseRedirect('index/?message=errorNoUsertoken')
		#得到时间戳
		#校验时间是否正确
		try:
			start_time=request.POST['start_time']
			end_time=request.POST['end_time']
			usertoken_s_timeStamp=get_unix(start_time)
			usertoken_e_timeStamp=get_unix(end_time)
		except Exception:
			return HttpResponseRedirect('index/?message=errorNoUsertokenTime')
		#存进session域中
		request.session['ausertoken']=ausertoken
		request.session['usertoken_s_timeStamp']=usertoken_s_timeStamp
		request.session['usertoken_e_timeStamp']=usertoken_e_timeStamp
	if request.method=='GET':
		ausertoken=request.session['ausertoken']
		usertoken_s_timeStamp=request.session['usertoken_s_timeStamp']
		usertoken_e_timeStamp=request.session['usertoken_e_timeStamp']
		
	uolists=Orders.objects.filter(usertoken='%s'%ausertoken,created_at__gt=usertoken_s_timeStamp,created_at__lt=usertoken_e_timeStamp).order_by('created_at')
	uolength=len(uolists)
	print(uolists)
	if uolength==0:
		return HttpResponseRedirect('index/?message=errorNoUser')
	#分页
	user_paginator=Paginator(uolists,25)
	if pindex=="":
		pindex=1
	else:
		pindex=int(pindex)
	#第i页实例对象
	user_page=user_paginator.page(pindex)

	return render(request,'htmls/result_usertoken.html',{'user_page':user_page,'uolength':uolength})"""
#根据用户标识查询某一范围时间的订单详情	
class Result_usertokenView(LoginRequiredMini,View):
	def get(self,request,pindex):
		ausertoken=request.session['ausertoken']
		usertoken_s_timeStamp=request.session['usertoken_s_timeStamp']
		usertoken_e_timeStamp=request.session['usertoken_e_timeStamp']
		uolists=Orders.objects.filter(usertoken='%s'%ausertoken,created_at__gt=usertoken_s_timeStamp,created_at__lt=usertoken_e_timeStamp).order_by('created_at')
		uolength=len(uolists)
		print(uolists)
		if uolength==0:
			return HttpResponseRedirect('index/?message=errorNoUser')
		#分页
		user_paginator=Paginator(uolists,25)
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		#第i页实例对象
		user_page=user_paginator.page(pindex)

		return render(request,'htmls/result_usertoken.html',{'user_page':user_page,'uolength':uolength})
	def post(self,request,pindex):
		ausertoken=request.POST['ausertoken']
		if not ausertoken:
			return HttpResponseRedirect('index/?message=errorNoUsertoken')
		#得到时间戳
		#校验时间是否正确
		try:
			start_time=request.POST['start_time']
			end_time=request.POST['end_time']
			usertoken_s_timeStamp=get_unix(start_time)
			usertoken_e_timeStamp=get_unix(end_time)
		except Exception:
			return HttpResponseRedirect('index/?message=errorNoUsertokenTime')
		#存进session域中
		request.session['ausertoken']=ausertoken
		request.session['usertoken_s_timeStamp']=usertoken_s_timeStamp
		request.session['usertoken_e_timeStamp']=usertoken_e_timeStamp
		uolists=Orders.objects.filter(usertoken='%s'%ausertoken,created_at__gt=usertoken_s_timeStamp,created_at__lt=usertoken_e_timeStamp).order_by('created_at')
		uolength=len(uolists)
		print(uolists)
		if uolength==0:
			return HttpResponseRedirect('index/?message=errorNoUser')
		#分页
		user_paginator=Paginator(uolists,25)
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		#第i页实例对象
		user_page=user_paginator.page(pindex)

		return render(request,'htmls/result_usertoken.html',{'user_page':user_page,'uolength':uolength})

#根据订单号查询订单

"""def result_orderno(request):
	orderno=request.POST['orderno']
	if not orderno:
		return HttpResponseRedirect('index/?message=errorNoOrderno')

	try:
		olist=Orders.objects.get(orderno='%s'%orderno)
	except Exception:
		return HttpResponseRedirect('index/?message=errorOrderno')
	return render(request,'htmls/result.html',{'olist':olist})"""

#根据订单号查询订单
class Result_ordernoView(LoginRequiredMini,View):
	def post(self,request):
		orderno=request.POST['orderno']
		if not orderno:
			return HttpResponseRedirect('index/?message=errorNoOrderno')

		try:
			olist=Orders.objects.get(orderno='%s'%orderno)
		except Exception:
			return HttpResponseRedirect('index/?message=errorOrderno')
		return render(request,'htmls/result.html',{'olist':olist})



#查询某段时间的订单是否发放成功

"""def is_filled(request):
	start_time=request.POST['start_time']
	end_time=request.POST['end_time']
	try:
		s_timeStamp=get_unix(start_time)
		e_timeStamp=get_unix(end_time)
	except Exception:
		return HttpResponseRedirect('index/?message=errorTime2')
	olist=Orders.objects.filter(Q(created_at__gt=s_timeStamp)&Q(created_at__lt=e_timeStamp)&Q(is_filled=0))
	if len(olist)==0:
		return HttpResponseRedirect('index/?message=errorOrderno2')
	if len(olist)>0:
		return HttpResponse("还有%s笔交易没有发放联金"%len(olist))
	else:
		return HttpResponse("联金都已经正常发放了")"""

#查询某段时间的订单是否发放成功
class Is_filledView(LoginRequiredMini,View):
	def post(self,request):
		start_time=request.POST['start_time']
		end_time=request.POST['end_time']
		try:
			s_timeStamp=get_unix(start_time)
			e_timeStamp=get_unix(end_time)
		except Exception:
			return HttpResponseRedirect('index/?message=errorTime2')
		olist=Orders.objects.filter(Q(created_at__gt=s_timeStamp)&Q(created_at__lt=e_timeStamp)&Q(is_filled=0))
		if len(olist)==0:
			return HttpResponseRedirect('index/?message=errorOrderno2')
		if len(olist)>0:
			return HttpResponse("还有%s笔交易没有发放联金"%len(olist))
		else:
			return HttpResponse("联金都已经正常发放了")



#注册
def register(request):
	if request.method=='GET':
		return render(request,'htmls/register.html')

	if request.method=='POST':

		username=request.POST.get('username')
		password=request.POST.get('password')
		user=User.objects.create_user(username=username,password=password)
		user.save()
		print("aaaa")
		return render(request,'htmls/isSucess.html')


#登录
"""def login(request):
	if request.method=='GET':
		return render(request,'htmls/login.html')


	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		#print(username)
		try:
			user=authenticate(username=username,password=password)
		except Exception:
			return HttpResponse('出错了')
		print(user)
		if user:
			login(request,user)
			print("aaa")
			return HttpResponseRedirect('orders.views.index')
		else:
			return HttpResponse('该用户不存在')

		user = auth.authenticate(username=username, password=password)
		print(1)
		print(user)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				
				return HttpResponseRedirect("/index")
			else:
				return HttpResponse("该用户不存在")
		else:
			return HttpResponse('该用户不存在')"""
class LoginView(View):
	def get(self,request):
		return render(request,'htmls/login.html')

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		#print(username)
		"""try:
			user=authenticate(username=username,password=password)
		except Exception:
			return HttpResponse('出错了')
		print(user)
		if user:
			login(request,user)
			print("aaa")
			return HttpResponseRedirect('orders.views.index')
		else:
			return HttpResponse('该用户不存在')"""

		user = auth.authenticate(username=username, password=password)
		print(1)
		print(user)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				next_url=request.GET.get('next',reverse('orders:index'))
				response=redirect(next_url)
				#return HttpResponseRedirect("/index")
				return response
			else:
				return HttpResponse("该用户不存在")
		else:
			return HttpResponse('该用户不存在')


def get_unix(times):
	timeArray=time.strptime(times,'%Y/%m/%d %H:%M:%S')
	timeStamp=int(time.mktime(timeArray))
	return timeStamp


def get_time(times):
	dt=time.strftime('%Y/%m/%d %H:%M:%S',times)
	return dt
