$(document).ready(function(){
    		var orderMethod=$("#orderMethod").val();
    		//获得当前时间戳
    		var token = $('input[name=csrfmiddlewaretoken]').val();
    		var end_timestamp =Date.parse(new Date())
    		//装换成当前时间
    		var end_time=timestampToTime(end_timestamp)
    		//获得过去一小时时间戳
    		var start_timestamp=end_timestamp-3600000;
    		//转化成过去一小时时间
    		setcookie('result_key',end_timestamp)
    		var start_time=timestampToTime(start_timestamp);
    		$("#startTime").val(start_time);
    		$("#endTime").val(end_time);
    		//url_test=
    		//页面加载自动查询过去一小时的全部订单
    		$.ajax({
    			url:"/result_time",
    			type:"get",
    			data: {
    					"orderMethod":orderMethod,
    					//csrfmiddlewaretoken: token,
						"start_timestamp":start_timestamp/1000,
						"end_timestamp":end_timestamp/1000,
						"orderMethod":1,
						"usertoken":0,
						"orderType":1,
						"orderno":0,
						"isfilled":3

						},
				success:function(data){
					$("#find").html("<a href='#' style='color: green' >查询成功！！！</a>")
					$("#a").html(data)
					
					
				}


    		})

    		$("#bt").click(function(){
    			$("#find").text("查询中。。。。")
    			$('#find').css('color','red')
    			//$.cookie("result_key",null);
    			//设置cookie为0
    			var now_timestamp =Date.parse(new Date())
    			setcookie('result_key',now_timestamp)
    			//获得开始时间戳和结束时间戳
    			var start_time=$("#startTime").val();
    			var end_time=$("#endTime").val();
    			//判断输入的时间格式是否正确
    			var reg=/^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$/;
    			var start_time_z=start_time.match(reg);
    			var end_time_z=end_time.match(reg);
    			//获得选择查询方式
				var orderMethod=$("#orderMethod").val();
				//获得用户标识
				var usertoken=$("#usertoken").val();
				if(usertoken==''){
					usertoken=0
				}
				//获得订单号
				var orderno=$("#orderno").val();
				if(orderno==''){
					orderno=0
				}
				//获得订单种类，分发联金状态
    			var orderType=$("#orderType").val();
    			var isfilled=$("#isfilled").val()
    			
				//根据选择查询方式不同，发送不同请求
				if(orderMethod=="0"){
					alert("查询方式必选，请选择一种")
				}
				
				//查询时间范围内的订单
				if(orderMethod=="1"){
					//开始时间，结束时间，订单种类，是否分发必填
					//alert("查询时间范围内订单")
					if(start_time_z==null){
    				 	alert("请输入正确的开始时间,开始时间必填")
					}
					if(end_time_z==null){
						alert("请输入正确的结束时间，结束时间必填")
					}
					//判断订单种类，分发联金状态是否选择
    				if(orderType=="0"){
    					alert("请选择订单种类")
    				};
    				if(isfilled=="4"){
    					alert("请选择分发联金状态")
    				};
					//输入的时间格式正确，转化成时间戳
 					var start_timestamp=timeToTimestamp(start_time);
 					var end_timestamp=timeToTimestamp(end_time);
 					if(start_timestamp!=null&&end_timestamp!=null&&orderType!=0&&isfilled!=4){


 					$.ajax({
						url: '/result_time',
						type: 'get',
						data: {
								"orderMethod":orderMethod,
								"start_timestamp":start_timestamp,
								"end_timestamp":end_timestamp,
								"usertoken":usertoken,
								"orderType":orderType,
								"orderno":orderno,
								"isfilled":isfilled

						},
						success: function (data) {
							$("#find").text("查询成功！！！")
							$("#find").css('color','green')
                			$("#a").html(data)
                			
            			}
        		})
 					}

				}

				//根据用户标识查询订单
				else if(orderMethod=="2"){
					//开始时间，结束时间，用户标识，订单种类，是否分发必填
					if(start_time_z==null){
    				 	alert("请输入正确的开始时间,开始时间必填")
					}
					if(end_time_z==null){
						alert("请输入正确的结束时间，结束时间必填")
					}
					//判断订单种类，分发联金状态是否选择
    				if(orderType=="0"){
    					alert("请选择订单种类")
    				};
    				if(isfilled=="4"){
    					alert("请选择分发联金状态")
    				};
    				if(usertoken==0){
    					alert('用户标识必填')
    				}
    				var start_timestamp=timeToTimestamp(start_time);
 					var end_timestamp=timeToTimestamp(end_time); 
    				if(start_timestamp!=null&&end_timestamp!=null&&isfilled!=4&&orderType!=4&&usertoken!=0){
    					$.ajax({
						url: '/result_time',
						type: 'get',
						data: {
								"orderMethod":orderMethod,
								"start_timestamp":start_timestamp,
								"end_timestamp":end_timestamp,
								"usertoken":usertoken,
								"orderType":orderType,
								"orderno":orderno,
								"isfilled":isfilled

						},
						success: function (data) {
							$("#find").text("查询成功！！！")
							$("#find").css('color','green')
                			$("#a").html(data)
                			
            			}
        		})
    				}

				}
				//根据订单号查询订单
				else if(orderMethod=="3"){
					//订单号必填
					if(orderno==0){
						alert("订单号必填")
					}
					if(orderno!=0){
						$.ajax({
						url: '/result_time',
						type: 'get',
						data: {
								"orderMethod":orderMethod,
								"start_timestamp":start_timestamp,
								"end_timestamp":end_timestamp,
								"usertoken":usertoken,
								"orderType":orderType,
								"orderno":orderno,
								"isfilled":isfilled

						},
						success: function (data) {
							$("#find").text("查询成功！！！")
							$("#find").css('color','green')
                			$("#a").html(data)
                			
            			}
        		});
					}
				}

    		});
    	});

		//设置cookie
		function setcookie(c_name,value){
			document.cookie=c_name+ "=" +escape(value);
		}
    	//得到时间
    	function timestampToTime(timestamp) {
     		var date = new Date(timestamp);//时间戳为10位需*1000，时间戳为13位的话不需乘1000
     		var Y = date.getFullYear() + '-';
     		var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
     		var D = date.getDate() + ' ';
     		var h = date.getHours();
     		if(h<10){
     			h='0'+h+ ':';;
     		}else{
     			h=h+ ':';
     		}
     		var m = date.getMinutes();
     		if(m<10){
     			m='0'+m+ ':';;
     		}else{
     			m=m+ ':';
     		}
     		var s = date.getSeconds();
     		if(s<10){
     			s='0'+s;
     		}else{
     			s=s;
     		}
     		return Y+M+D+h+m+s;
    	}
     	//得到时间戳
     	function timeToTimestamp(time){
     		var time_str=time+":000";
     		var s =time_str;
            s = s.replace(/-/g,"/");
     		var date = new Date(s);
		    // 有三种方式获
		    var timestamp =(Date.parse(date))/1000;
		    return timestamp;
     	}
   