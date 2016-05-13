from django.shortcuts import render

""" 
Create your views here.
Views are referenced by StationerryWebApp.urls
"""

from django.http import HttpResponse

def foo(request):
    return HttpResponse("Hello World!")

def home(request):
	return render(request, 'website/home.html', {})