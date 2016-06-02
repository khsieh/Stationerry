from django.shortcuts import render

# for user authentication, login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# for @login_required
from django.contrib.auth.decorators import login_required

# reference the Users model for user registration
from django.contrib.auth.models import User

# import utilities.py
from StationerryBackend.utilities import *

""" 
Create your views here.
Views are referenced by StationerryWebApp.urls
"""

LOGIN_URL = '/login/'
LOGIN_TEMPLATE = 'stationerry/login.html'
DASH_TEMPLATE = 'stationerry/dashboard.html'
ERRORS_TEMPLATE = 'stationerry/errors.html'
REGISTER_TEMPLATE = 'stationerry/register.html'

currUser = None

# This is the homepage
def home(request):
    return render(request, LOGIN_TEMPLATE, {})

# This is for the user sign up / registration
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']


    	User.objects.create (
            first_name = name,
            username = username,
            password = password,
            email = email
        )


        # this fixes the password issue because
        # set_password(raw_input) hashes the raw input passed in
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return HttpResponse('New user created.')



    return render(request, REGISTER_TEMPLATE, {})

# This is the user authentication 
def userLogin(request):
    errMessage = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # check if user is in our userbase
        if user is not None:
            # in the Django admin thingy, there's a tick mark for (in)activeness
            # if user is inactive, can't log in
            if user.is_active:
                currUser = user
                login(request, user)
                return HttpResponseRedirect("/dashboard/")

            else:
                errMessage = "Your account is deactivated."

        else:
            errMessage = "Invalid username or password."

    # first param is the request, second is the template, third is a variable to be passed to template
    return render(request, LOGIN_TEMPLATE, {"errMessage":errMessage})

def userLogout(request):
    currUser = None
    logout(request)
    return HttpResponseRedirect(LOGIN_URL)

# This is the main page after the user logs in.
@login_required
def dashboard(request):
    return render(request, DASH_TEMPLATE, {})

"""
http://stackoverflow.com/questions/22108082/how-to-pass-a-list-from-a-view-to-template-in-django
http://stackoverflow.com/questions/8949834/django-how-do-i-iterate-through-a-list-of-dictionaries-to-concatenate-values-f
"""
@login_required
def errors(request):
    errorList = []
    searchQuery = ""
    hideResults = True

    if 'q' in request.GET:
        # check if the GET request named 'q' has an empty value
        if request.GET['q'] == '':
            print 'ERRORS.HTML: Nothing was entered.' 
            hideResults = True
        # if not empty, probabably a valid search query. fetch all matching
        # results from db in a list of dictionaries
        else:
            print 'ERRORS.HTML: You searched for ' + request.GET['q']
            book1 = {'title':'The Great Whale', 'author':'Wailord', 'year': '2014'}
            book2 = {'title':'Flying Pig', 'author':'Piggie', 'year': '2016'}
            errorList.append(book1)
            errorList.append(book2) 
            hideResults = False
            searchQuery = request.GET['q']


    return render(request, ERRORS_TEMPLATE, {"errorList" : errorList, "hideResults" : hideResults, "searchQuery" : searchQuery})
