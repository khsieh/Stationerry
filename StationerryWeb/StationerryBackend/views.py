import sqlite3
import json

from django.shortcuts import render
from django.http import HttpResponse
import StationerryBackend.models

def index(request) :
    return HttpResponse("You shouldn't be here.")

def recievereport(request) :
    if request.method != POST :
        raise PermissionDenied
    raw_data = request.body
    data = json.load(raw_data)
    insertReportIntoDB(data['name'], data['version'], data['platform'], data['type'], data['report'])

def getquery(request) :
    pass

def insertReportIntoDB(AppName, AppVersion, iPlatform, ReportType, Report) :
    AppSet = App.objects.filter(App_Name=AppName)
    if len(AppSet) is 0 :
        return HttpResponse("No entry for an app with that name exist!")
    TargetPlatform = AppSet.filter(Platform=iPlatform)
    if len(TargetPlatform) is 0:
        return HttpResponse("No entry for an app on target platform exist.")
    try :
        TargetAppVersion = AppSet.get(App_Version=AppVersion)
        NewReport = BugReport(Error_Type=ReportType, Error_Message=Report)
        NewReport.App_Name = TargetAppVersion
        NewReport.save()
    except:
        return HttpResponse("No entry for that app version exist.")
        
