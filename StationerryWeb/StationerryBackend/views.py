import sqlite3
import json

from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return HttpResponse("You shouldn't be here.")

def recievereport(request) :
    raw_data = request.body
    data = json.load(raw_data)
    insertReportIntoDB(data['name'], data['version'], data['platform'], data['type'], data['report'])

def connectToDatabase(DB_NAME) :
    pass
    
def getquery(request) :
    pass

def insertReportIntoDB(AppName, AppVersion, Platform, ReportType, Report) :
    pass
