from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),    
    url(r'^sendreport$', views.recievereport, name = 'send'),
    url(r'^getreport$', views.getquery, name = 'get'),
    url(r'^testbench$', views.testBench, name = 'test'),
]

