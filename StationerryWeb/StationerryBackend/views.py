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
import re

from django.template import loader

def index(request) :
    return HttpResponse("You shouldn't be here.")

@csrf_exempt
def recievereport(request) :
    if request.method != 'POST':
        raise django.core.exceptions.PermissionDenied()
    raw_data = request.body
    try :
        # data is sent as a json object
        data = json.loads(raw_data)
        insertDB = insertReportIntoDB(data['CUSTOM_DATA']["AppName"], data['BUILD_CONFIG']['VERSION_NAME'], data['BUILD']['VERSION']['RELEASE'], "Exception", data['STACK_TRACE'], data['BRAND'], data['PHONE_MODEL'], "Android")
        return insertDB
    except :
        # data is just a long byte stream according to a specific format.
        Body = ""
        AppName = ""
        Version = ""
        Platform = ""
        BugType = "Exception"
        Brand = ""
        Model = ""
        OS = ""
        for line in raw_data.splitlines(True) :
            Body = Body + line
            matchData = re.match("AppName = ", line)
            if matchData :
                AppName = line[matchData.end():]
            matchData = re.match("APP_VERSION_NAME=", line)
            if matchData :
                Version = line[matchData.end():]
            matchData = re.match("ANDROID_VERSION=", line)
            if matchData :
                OS = line
                Platform = line[matchData.end():]
            matchData = re.match("PHONE_MODEL=", line)
            if matchData :
                Model = line[matchData.end():]
            matchData = re.match("BRAND=", line)
            if matchData :
                Brand = line[matchData.end():]
        insertDB = insertReportIntoDB(AppName, Version, Platform, BugType, Body, Brand, Model, OS)
        return insertDB
    return HttpResponse("Error inserting bug report.")


def getquery(request) :
    pass

def insertReportIntoDB(AppName, AppVersion, iPlatform, ReportType, Report, Brand, DeviceModel, ModelOS) :
    
    AppName = AppName.rstrip()
    AppVersion = AppVersion.rstrip()
    iPlatform = iPlatform.rstrip()
    ReportType = ReportType.rstrip()
    Report = Report.rstrip()
    Brand = Brand.rstrip()
    DeviceModel = DeviceModel.rstrip()
    ModelOS = ModelOS.rstrip()

    AppSet = App.objects.all()
    '''
    for a in AppSet:
        m = (AppName == a.App_Name)
        #print type(a.App_Name)
        print AppName + " is " + a.App_Name
    ''' 
    #print "Length of AppSet: " + len(AppSet)
    if len(AppSet) is 0 :
        return HttpResponse("No entry for an app with that name exist!")
    
    print "Before All Filters:"
    print AppSet

    #First filter: App Name
    FilterSet1 = []
    for a in AppSet:
        matchedName = (AppName == a.App_Name)
        if matchedName:
            FilterSet1.append(a)
    
    #Second filter: App Version
    FilterSet2 = []
    for f in FilterSet1:    
        matchedVersion = (AppVersion == f.App_Version)
        if matchedVersion:
            FilterSet2.append(f)

    #Third filter: App Platform
    FilterSet3 = []
    for f in FilterSet2:
        matchedPlatform = (iPlatform == f.Platform)
        if matchedPlatform:
            FilterSet3.append(f)
    
    if len(FilterSet3) is 0:
        return HttpResponse("No entry for an app on target platform exist.")
    try :
        
        TargetAppVersion = FilterSet3[0]
        NewReport = BugReport(Error_Type=ReportType, Error_Message=Report, Model_Name=Brand, Model_OS=ModelOS, Device_Model=DeviceModel)
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
    t = loader.get_template('/home/kevhsieh/Stationerry/StationerryWeb/StationerryWebApp/templates/stationerry/testbench.html')
    return HttpResponse(user.User_Name)

def testBench3(request) :
    return HttpResponse(util.getParseHTML("apphello", "3.2.1", "0", ""))

def testBench4(request) :
    return HttpResponse(util.findError("apphello"))
