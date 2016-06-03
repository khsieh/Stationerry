#!/usr/bin/python

import re
import sys
import models as m
from django.contrib.auth.models import User

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
        #first regex rule, look for the string "exception"
            matched = re.search(SearchString,line,re.I)
            if matched:
                matchedlines.append(line)
        #add more rules, what are we looking for exactly
        #can add more if statements for filters in the beginning if we know what language or platform we're dealing with.
    return matchedlines

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

def getAllErrors(errorString, user) :
    
    appSet = m.App.objects.filter(username=user)
    reportSet = m.BugReport.objects.all()
    userList = []
    for app in appSet:
        for report in reportSet:
            if (app.App_Name == report.App_Name.App_Name):
                userList.append(report)
    userSet = list(set(userList))

    logList = []
    for report in userSet:
        report_lines = report.Error_Message.split('\n')
        for line in report_lines:
            if re.search(errorString, line, re.I) :
                tempDict = {}
                tempDict['time'] = str(report.Time.month) + "/" + str(report.Time.day) + "/" + str(report.Time.year) + ", " + str(report.Time.hour) + ":" + str(report.Time.minute) + ":" + str(report.Time.second)
                tempDict['error_type'] = report.Error_Type
                tempDict['error_msg'] = line
                tempDict['status'] = report.Status
                tempDict['device_model'] = report.Device_Model
                app = m.App.objects.get(id=report.App_Name_id)
                tempDict['app_name'] = app.App_Name
                tempDict['app_version'] = app.App_Version
                tempDict['device_os'] = app.Platform
                logList.append(tempDict)
    return logList
    
def errorFilters(errorString, errorType, appName, appVersion, osSys, devModel, user) :
    
    #regex matching variables
    stringMatch=False
    typeMatch=False
    appNameMatch=False
    appVersionMatch=False
    osSysMatch=False
    devModelMatch=False
    
    appSet = m.App.objects.filter(username=user)
    reportSet = m.BugReport.objects.all()

    userList = []
    for app in appSet:
        for report in reportSet:
            if (app.App_Name == report.App_Name.App_Name):
                userList.append(report)
    userSet = list(set(userList))

    logList = []
    for report in userSet:
        if errorType:
            typeMatch = re.search(errorType, report.Error_Type,re.I)
        else:
            typeMatch = True
            
        if appName:
            appNameMatch = re.search(appName, report.App_Name,re.I)
        else:
            appNameMatch = True
            
        if appVersion:
            appVersionMatch = re.search(appVersion, report.App_Version, re.I)
        else:
            appVersionMatch = True

        if osSys:
            osSysMatch = re.search(osSys, report.Model_OS, re.I)
        else:
            osSysMatch = True

        if devModel:
            devModelMatch = re.search(devModel, report.Device_Model, re.I)
        else:
            devModelMatch = True

        if errorString:
            report_lines = report.Error_Message.split('\n')
            for line in report_lines:
                stringMatch = re.search(errorString, line, re.I)
                if stringMatch:
                    if typeMatch and appNameMatch and appVersionMatch and osSysMatch and devModelMatch:
                        tempDict = {}
                        tempDict['time'] = str(report.Time.month) + "/" + str(report.Time.day) + "/" + str(report.Time.year) + ", " + str(report.Time.hour) + ":" + str(report.Time.minute) + ":" + str(report.Time.second)
                        tempDict['error_type'] = report.Error_Type
                        tempDict['error_msg'] = line
                        tempDict['status'] = report.Status
                        tempDict['device_model'] = report.Device_Model
                        app = m.App.objects.get(id=report.App_Name_id)
                        tempDict['app_name'] = app.App_Name
                        tempDict['app_version'] = app.App_Version
                        tempDict['device_os'] = app.Platform
                        logList.append(tempDict)
    return logList

def getTimeErrors(timeString, user) :
    
    appSet = m.App.objects.filter(username=user)
    reportSet = m.BugReport.objects.all()
    userList = []

    if len(appSet) > 0:
        for report in reportSet:
            userList.append(report)

    userSet = list(set(userList))

    logList = []

    for report in userSet:
        if re.search(timeString, str(report.Time), re.I):
            report_lines = report.Error_Message.split('\n')
            for line in report_lines:
                if re.search("Exception", line, re.I):
                    logList.append(line)
    
    return logList

def getUniqErrors(user) :
    
    appSet = m.App.objects.filter(username=user)
    reportSet = m.BugReport.objects.all()

    userList = []
    for app in appSet:
        for report in reportSet:
            if (app.App_Name == report.App_Name.App_Name):
                userList.append(report)
    userSet = list(set(userList))

    logList = []
    for report in userSet:
        report_lines = report.Error_Message.split('\n')
        for line in report_lines:
            stringMatch = re.search("Exception", line, re.I)

            # if match, append
            if stringMatch:
                logList.append(line)

    return list(set(logList))

def getKey(item):
    return item[1]

def getTop5(user):
    appSet = m.App.objects.filter(username=user)
    reportSet = m.BugReport.objects.all()

    
    top5 = {}

    userList = []
    for app in appSet:
        for report in reportSet:
            if (app.App_Name == report.App_Name.App_Name):
                userList.append(report)
    userSet = list(set(userList))

    for report in userSet:
        report_lines = report.Error_Message.split('\n')
        for line in report_lines:
            stringMatch = re.search("Exception", line, re.I)

            if stringMatch:
                if top5.has_key(line):
                    # print line
                    top5[line] += 1
                else:
                    top5[line] = 1

    top5List = []

    for key, val in top5.iteritems():
        entry = []
        entry.append(key)
        entry.append(val)
        top5List.append(entry)

    sorted(top5List, key=getKey, reverse=True)
    del top5List[5:]

    return top5List