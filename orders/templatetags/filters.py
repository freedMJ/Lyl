from django.template import Library
import time

register=Library()



@register.filter
def get_times(times):
	new_times=time.localtime(times)
	dt=time.strftime('%Y-%m-%d %H:%M:%S',new_times)
	return dt
