# -*- coding: utf-8 -*-  
'''
Created on 2014年10月1日

@author: gaomh
'''
import datetime
import logging
import subprocess
from urllib2 import URLError
import urllib2


def getResult(url):
    result = ''
    try:
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        result = res.read()
    except URLError, e:
        logging.info(e)
    return result

def getCmdRes(cmd):
    p = subprocess.Popen(cmd, shell = True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    cmdRes = p.stdout.readlines()
    return cmdRes

def dateTimeToStr(dateTime):
    timeStr = ''
    if not dateTime:
        return timeStr
    try:
        timeStr = dateTime.strftime('%Y-%m-%d')
    except Exception, e:
        logging.info(e)
        return timeStr

    return timeStr

def strToDateTime(arise_time):
    fomat_datetime = ''
    try:
        fomat_datetime = datetime.datetime.strptime(arise_time, '%Y-%m-%d')
    except ValueError, e:
        logging.info(e)
        return None
    return fomat_datetime