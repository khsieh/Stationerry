from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Django will give each model an unique ID as a primary key
# when we do not specify one. (^_^)

# Defines for Django - makes schema for app - set the database
class App(models.Model) :
    App_Name = models.TextField()
    App_Version = models.TextField()
    Platform = models.TextField()
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owns')

    def __unicode__(self) :
        return self.App_Name + " " + self.App_Version

# schema for bugreport
class BugReport(models.Model) :
    Model_Name = models.TextField() 
    Model_OS = models.TextField()
    Error_Type = models.TextField()
    Error_Message = models.TextField()
    Time = models.DateTimeField(auto_now=True)
    Status = models.TextField()
    Device_Model = models.TextField()
    App_Name = models.ForeignKey(App, on_delete=models.CASCADE, related_name='Name')

    def __unicode__(self) :
        return self.App_Name + " " + self.Model_Name + " " + self.Model_OS + " :" + self.Error_Message
