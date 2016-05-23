from __future__ import unicode_literals

from django.db import models

# Django will give each model an unique ID as a primary key
# when we do not specify one. (^_^)

class App(models.Model) :
    App_Name = models.TextField()
    App_Version = models.TextField()
    Platform = models.TextField()

    def __unicode__(self) :
        return self.App_Name + " " + self.App_Version
    pass

class BugReport(models.Model) :
    Error_Type = models.TextField()
    Error_Message = models.TextField()
    Time = models.DateTimeField(auto_now=True)
    App_Name = models.ForeignKey(App, on_delete=models.CASCADE, related_name='Name')

    def __unicode__(self) :
        return self.App_Name + " " + self.App_Version + " :" + self.App_Message
