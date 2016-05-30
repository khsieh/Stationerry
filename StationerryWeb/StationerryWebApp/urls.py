""" 
This file contains the actual urls that will be used for the site.
References views in StationerryWebApp.views which tell you which html file to display.

In Android Studio, it's similar to doing
setContentView(R.layout.xml_file);
Which tells you to use a specific xml file to display for the current activity / fragment.

However, it's a 3 part step (compared to two for Android).
url -> views -> html file.

Guide: http://tutorial.djangogirls.org/en/django_urls/

Patterns for URL:
^ for beginning of the text
$ for end of text
\d for a digit
+ to indicate that the previous item should be repeated at least once
() to capture part of the pattern

Imagine you have a website with the address like that: http://www.mysite.com/post/12345/, 
where 12345 is the number of your post.

Writing separate views for all the post numbers would be really annoying. With regular expression
we can create a pattern that will match the url and extract the number for us: ^post/(\d+)/$. 
Let's break it down piece by piece to see what we are doing here:

    ^post/ is telling Django to take anything that has post/ at the beginning of the url (right after ^)
    (\d+) means that there will be a number (one or more digits) and that we want the number captured and extracted
    / tells django that another / character should follow
    $ then indicates the end of the URL meaning that only strings ending with the / will match this pattern

"""

"""
Some guy used but idk what it does.
from django.contrib import admin
admin.autodiscover()

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userLogin, name='home'),
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^errors/$', views.errors, name='errors'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]