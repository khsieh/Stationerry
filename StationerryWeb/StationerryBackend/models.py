from __future__ import unicode_literals

from django.db import models

# Django will give each model an unique ID as a primary key
# when we do not specify one. (^_^)

class Users(models.Model) :
    Real_Name = models.TextField()
    User_Name = models.TextField(primary_key=True)
    Password = models.TextField()
    Email = models.TextField()
    
    def __unicode__(self) :
        return self.User_Name

# Defines for Django - makes schema for app - set the database
class App(models.Model) :
    App_Name = models.TextField()
    App_Version = models.TextField()
    Platform = models.TextField()
    App_Name = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Name')

    def __unicode__(self) :
        return self.App_Name + " " + self.App_Version

# schema for bugreport
class BugReport(models.Model) :
    Model_Name = models.TextField() 
    Model_OS = models.TextField()
    Error_Type = models.TextField()
    Error_Message = models.TextField()
    Time = models.DateTimeField(auto_now=True)
    App_Name = models.ForeignKey(App, on_delete=models.CASCADE, related_name='Name')

    def __unicode__(self) :
        return self.App_Name + " " + self.Model_Name + " " + self.Model_OS + " :" + self.Error_Message
