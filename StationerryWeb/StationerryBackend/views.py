import sqlite3
import json

from django.shortcuts import render
from django.http import HttpResponse
import StationerryBackend.models

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import django.core.exceptions
from models import App
from models import BugReport
import utilities as util

from django.template import loader

def index(request) :
    return HttpResponse("You shouldn't be here.")

@csrf_exempt
def recievereport(request) :
    if request.method != 'POST':
        raise django.core.exceptions.PermissionDenied()
    raw_data = request.body
    data = json.loads(raw_data)
    insertDB = insertReportIntoDB(data['name'], data['version'], data['platform'], data['type'], data['report'])
    return insertDB

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
        return HttpResponse("Success")
    except :
        return HttpResponse("No entry for that app version exist.")
        

def testBench(request) :
    grab_list = []
    try : 
        print util.parse("apphello", "3.2.1", "0")
        grab_list = util.parse("apphello", "3.2.1", "0")
        grab_list = ["foo", "bar", "baz"]
    except :
        return HttpResponse("No lines found")
    lineString = ""
    for line in grab_list :
        lineString = lineString + line + "<br>"
    #t = loader.get_template('/home/kawaii5/Stationerry/StationerryWeb/StationerryWebApp/templates/stationerry/testbench.html')
    return HttpResponse(lineString)

def testBench2(request) :
    grab_dict = {}
    user = 0
    try :
        print util.findUser("user")
        user= util.findUser("user")
    except :
        pass
    t = loader.get_template('/home/kawaii5/Stationerry/StationerryWeb/StationerryWebApp/templates/stationerry/testbench.html')
    return HttpResponse(user.User_Name)

def testBench3(request) :
    return HttpResponse(util.getParseHTML("apphello", "3.2.1", "0", ""))
