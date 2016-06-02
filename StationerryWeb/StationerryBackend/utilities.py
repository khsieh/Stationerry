#!/usr/bin/python

import re
import sys
import models as m

def parse(AppName, AppVersion, AppPlatform, SearchString) :
    loglist = []
    matchedlines = []
    targetApp = m.App.objects.get(App_Name=AppName,App_Version=AppVersion,Platform=AppPlatform) 
    reportSet = m.BugReport.objects.filter(App_Name=targetApp.pk)
    report = reportSet.first()
    while not (report == reportSet.last()) :
        print report.Error_Message
        loglist.append(report.Error_Message)
        report = reportSet.iterator()
    loglist.append(report.Error_Message)
    for logfile in loglist:
        for line in logfile.split('\n') :
            print line
        #first regex rule, look for the string "exception"
            matched = re.search(SearchString,line,re.I)
            if matched:
                matchedlines.append(line)
        #add more rules, what are we looking for exactly
        #can add more if statements for filters in the beginning if we know what language or platform we're dealing with.
    return matchedlines


def findUser(username) :
    user = 0
    try :
        #user = m.Users.objects.get(User_Name=username)
        pass
    except :
        user = 0
    return user


def getParseHTML(AppName, AppVersion, AppPlat, SearchString) :
    grab_list = []
    try : 
        grab_list = parse(AppName,AppVersion,AppPlat,SearchString)
    except :
        return "No lines found"
    lineString = ""
    for line in grab_list :
        lineString = lineString + line + "<br>"
    return lineString

#from db, output app name, app ver, and platform
def findError(SearchString) :
    loglist = []
    matchedlines = []
    apps = []
    reportSet = m.BugReport.objects.all()
    
    report = reportSet.first()
    while not (report == reportSet.last()) :
        if m.App.objects.get(pk=report.App_Name_id).App_Name:
            apps.append(m.App.objects.get(id=report.App_Name_id))
            #loglist.append(m.App.objects.get(id=report.App_Name_id).App_Name)
            #print m.App.objects.get(id=report.App_Name_id).App_Name
        report = reportSet.iterator()
    apps.append(m.App.objects.get(id=report.App_Name_id))
    #loglist.append(m.App.objects.get(id=report.App_Name_id).App_Name)
    #print m.App.objects.get(id=report.App_Name_id).App_Name
    
    for app in apps:
        #print line
        line = app.App_Name
        matched = re.search(SearchString,line,re.I)
        if matched:
            line = "App Name: " + app.App_Name + "App Version: " + app.App_Version + " App Platform: " + app.Platform
            matchedlines.append(line)
    return matchedlines
    

def getAllErrors(errorString) :
    logList = []
    reportSet = m.BugReport.objects.all()
    for report in reportSet :
        for line in report.Error_Message :
            if re.search(errorString, line) :
                tempDict = {}
                tempDict['time'] = str(report.Time.month) + " " + str(report.Time.day) + " " + str(report.Time.year) + " " + \
                                   str(report.Time.hour) + " " + str(report.Time.minute) + " " + str(report.Time.second) + " " + \
                                   str(report.Time.mircosecond)
                tempDict['error_type'] = report.Error_Type
                tempDict['error_msg'] = report.Error_Message
                tempDict['status'] = report.Status
                tempDict['device_model'] = report.Device_Model
                app = m.App.objects.get(id=report.App_Name_id)
                tempDict['app_name'] = app.App_Name
                tempDict['app_version'] = app.App_Version
                tempDict['device_os'] = app.Platform
                logList.append(tempDict)
                break
    return logList
    
