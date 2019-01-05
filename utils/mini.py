from django.contrib.auth.decorators import login_required

class LoginRequiredMini(object):
	@classmethod
	def as_view(cls,**initkwargs):
		view=super(LoginRequiredMini,cls).as_view(**initkwargs)
		return login_required(view)