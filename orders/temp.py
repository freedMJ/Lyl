#查询某一段时间的订单	
class ResultView(LoginRequiredMini,View):
	def get(self,request,pindex):
		print("0000")
		orderMethod=1
		a=request.session.get("a")
		if a is None:
			a="none"
		key_str='result_time_%s_%s'%(orderMethod,a)
		flage=cache.has_key(key_str)		
		print(flage)
		if flage:
			print("xxxxxx")		
			try:
				olist=cache.get(key_str)
			except Exception as e:
				return HttpResponse("数据查询失败")

		else:
			print("yyyyyyy")
			orderMethod=request.GET.get('orderMethod')
			print("1%s"%orderMethod)
			start_time_stamp=int(request.GET.get("start_timestamp"))
			end_time_stamp=int(request.GET.get("end_timestamp"))
			if not all([start_time_stamp,end_time_stamp]):
				return HttpResponse("开始时间与结束时间必填")
			usertoken=request.GET.get("usertoken")#	用户标识 选填
			orderno=request.GET.get("orderno")#订单号 选填
			orderType=request.GET.get("orderType")#订单种类 必填
			isfilled=int(request.GET.get("isfilled"))#是否已分发 必填
			print(start_time_stamp)
			print(end_time_stamp)
			print(usertoken)
			print(orderno)
			print(orderType)
			print(isfilled)
			try:
				olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,isfilled='%s'%isfilled)
			except Exception as e:
				return HttpResponse("查询失败")
			print(olist)
			"""
			#if all([start_time_stamp,end_time_stamp,orderType,isfilled]):
				
				if orderno is None and usertoken is None:
					alert("000000000000000000000000000000000000")
					olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,isfilled='%d'%isfilled)
					a='%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,orderType,isfilled)
			try:
				#选择条件执行
				#查询该段时间所有订单
				if all([start_time_stamp,end_time_stamp,orderType,isfilled]) and orderno is None and usertoken is None:
					alert("000000000000000000000000000000000000")
					olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,isfilled='%d'%isfilled)
					a='%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,orderType,isfilled)

				if all([start_time_stamp,end_time_stamp,usertoken,orderType,isfilled]) and orderno is None:
				#查询该段时间该用户的所有订单
					if orderType=='1':
						olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,usertoken='%s'%usertoken)
						a='%s_%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,usertoken,orderType,isfilled)
				#查询该段时间该用户的按摩枕订单
					elif orderType=='2':
						olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,usertoken='%s'%usertoken,orderno__contains='LYL2')
						a='%s_%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,usertoken,orderType,isfilled)
				#查询该段时间该用户的游戏订单
					elif orderType=='3':
						olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,usertoken='%s'%usertoken,orderno__contains='LYLGD')
						a='%s_%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,usertoken,orderType,isfilled)
			#查询该段时间的某一个订单
				if all([start_time_stamp,end_time_stamp,orderno,orderType,isfilled]) and usertoken is None:
					olist=Orders.objects.filter(created_at__gt='%s'%start_time_stamp,created_at__lt='%s'%end_time_stamp,ordern='%s'%orderno)
					a='%s_%s_%s_%s_%s'%(start_time_stamp,end_time_stamp,orderno,orderType,isfilled)
			except Exception as e:
				return HttpResponse("查询失败")
				
			#把查询到的数据存入redis数据库中
			try:
				print("aaa")
				key='result_time_%s_%s'%(orderMethod,a)
				print(key)
				#request.session['a']=a
				cache.set(key,olist,60*60)
			except Exception as e:
				return HttpResponse("数据保存失败")
				"""
			
			
		print(olist)
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

		#return render(request,'htmls/result_list.html',{'page':page,'page_list':page_list,'olength':olength,'len_pindex':len_pindex})
		return render(request,'htmls/template.html',{'page':page,'page_list':page_list,'olength':olength,'len_pindex':len_pindex})
		"""
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
		paginator=Paginator(olist,constants.HTML_PAGE_NUMS) #每页5条
		if pindex=="":
			pindex=1
		else:
			pindex=int(pindex)
		page=paginator.page(pindex)

		total_page_number=paginator.num_pages
		len_pindex=math.ceil(float(olength/constants.HTML_PAGE_NUMS))
		page_list=get_page.get_pages(int(total_page_number),int(pindex))

		return render(request,'htmls/result_list.html',{'page':page,'page_list':page_list,'olength':olength,'len_pindex':len_pindex})"""
