from django.shortcuts import render
from django.views.generic import View
from user_profile.models import User
from models import Tweet
# Create your views here.

class Index(View):
	def get(self, request):
		params = {}
		params['name'] = "Django"
		return render(request, 'base.html', params)

class Profile(View):
	"""
	User profile reachable from /user/<username> URL
	"""
	
	def get(self, request, username):
		params = dict()
		user = User.objects.get(username=username)
		tweets = Tweet.objects.filter(user=user)
		params["tweets"] = tweets
		params["user"] = user
		return render(request, 'profile.html', params)



