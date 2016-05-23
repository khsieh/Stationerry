from django.shortcuts import render

# for user authentication, login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# for @login_required
from django.contrib.auth.decorators import login_required

""" 
Create your views here.
Views are referenced by StationerryWebApp.urls
"""

LOGIN_URL = '/login/'
LOGIN_TEMPLATE = 'stationerry/login.html'
MAIN_TEMPLATE = 'stationerry/base.html'
STATS_TEMPLATE = 'stationerry/stats.html'

def foo(request):
    return HttpResponse("Hello World!")

# This is the homepage
def home(request):
	return render(request, LOGIN_TEMPLATE, {})

# This is the user authentication 
def userLogin(request):
	"""
	References: 
	https://www.youtube.com/watch?v=yTK_Kx1Qoqc

	next = request.GET.get('next', '/main/')

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		# check if user is in our userbase
		if user is not None:

			# in the Django admin thingy, there's a tick mark for (in)activeness
			# if user is inactive, can't log in
			if user.is_active
				login(request, user)
				return HttpResponseRedirect(next)

			else:
				return HttpResponse("Inactive user.")

		else:
			return HttpResponseRedirect(LOGIN_URL)

	"""
	# first param is the request, second is the template, third is a variable to be passed to template
	# return render(request, 'stationerry/login.html', {'redirect_to': next})
	return render(request, LOGIN_TEMPLATE, {})

def logout(request):
	# logout(request)
	return HttpResponseRedirect(LOGIN_URL)

# This is the main page after the user logs in.
# @login_required
def main(request):
	return render(request, MAIN_TEMPLATE, {})

def stats(request):
	return render(request, STATS_TEMPLATE, {})
