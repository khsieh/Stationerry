from django.shortcuts import render

""" 
Create your views here.
Views are referenced by StationerryWebApp.urls
"""

from django.http import HttpResponse

def foo(request):
    return HttpResponse("Hello World!")

# This is the homepage
def home(request):
	return render(request, 'stationerry/login.html', {})

def login(request):
	return render(request, 'stationerry/login.html', {})

# This is the main page after the user logs in
def main(request):
	return render(request, 'stationerry/base.html', {})