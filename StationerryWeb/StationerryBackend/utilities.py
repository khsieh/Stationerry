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
        user = m.Users.objects.get(User_Name=username)
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

def findError(SearchString) :
    loglist = []
    matchedlines = []
    reportSet = m.BugReport.objects.all()
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


