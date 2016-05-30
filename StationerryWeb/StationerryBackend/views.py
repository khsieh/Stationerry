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
import parser_func as pf

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
    except:
        return HttpResponse("No entry for that app version exist.")
        

def testBench(request) :
    print pf.parse("apphello", "3.2.1", "0")

    grab_list = pf.parse("apphello", "3.2.1", "0")
    grab_dict = {'list' : grab_list}
    json_format = json.dumps(grab_dict)
    print "json format: "
    print json_format
    t = loader.get_template('/home/kawaii5/Stationerry/StationerryWeb/StationerryWebApp/templates/stationerry/testbench.html')
    return HttpResponse(t.render(grab_dict, request), content_type="application/json")
