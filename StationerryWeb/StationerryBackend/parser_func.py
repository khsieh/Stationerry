#!/usr/bin/python

import re
import sys
import models as m

def parse(AppName, AppVersion, AppPlatform) :
    loglist = []
    matchedlines = []
    targetApp = m.App.objects.get(App_Name=AppName,App_Version=AppVersion,Platform=AppPlatform) 
    reportSet = m.BugReport.objects.filter(App_Name=targetApp.pk)
    report = reportSet.first()
    print "SOMETHING"
    while not (report == reportSet.last()) :
        print report.Error_Message
        loglist.append(report.Error_Message)
        report = reportSet.iterator()
    print "we have reached the next for loop"
    loglist.append(report.Error_Message)
    for logfile in loglist:
        print "in for loop 1"
        for line in logfile.split('\n') :
            print line
        #first regex rule, look for the string "exception"
            matched = re.search('(.*exception)',line,re.I)
            if matched:
                print "in for loop 2"
                matchedlines.append(matched.group())
        #add more rules, what are we looking for exactly
        #can add more if statements for filters in the beginning if we know what language or platform we're dealing with.
    return matchedlines
