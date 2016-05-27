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
DASH_TEMPLATE = 'stationerry/dashboard.html'
STATS_TEMPLATE = 'stationerry/stats.html'
REGISTER_TEMPLATE = 'stationerry/register.html'

def foo(request):
    return HttpResponse("Hello World!")

# This is the homepage
def home(request):
	return render(request, LOGIN_TEMPLATE, {})

# This is for the user sign up / registration
def register(request):
	return render(request, REGISTER_TEMPLATE, {})

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
def dashboard(request):
	return render(request, DASH_TEMPLATE, {})

"""
This sounds a bit dumb... but it should theoretically work.
I could perform a query to a database here, and store that
information into a dictionary. Then do json.dumps(data) to
pass it to the html page. And then use js to display the charts
using Chart.js's API.

I guess we'll have a utilities.py, which will fetch data from the database.
I'll call that function and do json.dump(data).

http://stackoverflow.com/questions/34777794/django-show-graphs-with-chartjs
http://stackoverflow.com/questions/6467812/how-to-return-a-dictionary-in-python-django-and-view-it-in-javascript

How do I update the chart if the user presses the reload/refresh button though?
I guess something similar to the login thing??
"""
def stats(request):
	return render(request, STATS_TEMPLATE, {})
