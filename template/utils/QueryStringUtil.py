# -*- coding: utf-8 -*-  

'''
Created on 2013-7-3

@author: gaott
'''
from collections import OrderedDict
import hashlib
import time
import urllib

def creatQueryString(params):
    if not params:
        return ''
    if len(params) <= 0:
        return''
    
    #对参数进行排序
    l = []
    #遍历字典，进行quote_plus操作，并把所有字段拼成list
    for k in params:
        k = urllib.quote(str(k))
        v = urllib.quote(str(params[k]))
        url_param = '%s=%s' % (k, v)
        l.append(url_param)
    l.sort()
    
    return '&'.join(l)

def createHashQueryString(params, salt, currentTime):
    paramStr = creatQueryString(params)
    
    htqs = ''
    hashStr = ''
    
    if paramStr:
        queryStr = '%s&time=%s&salt=%s' % (paramStr, currentTime, salt)
        hashStr = hashlib.sha1(queryStr).hexdigest()
        htqs = '%s&time=%s&hash=%s' % (paramStr, currentTime, hashStr)
    else:
        queryStr = 'time=%s&salt=%s' % (currentTime, salt)
        hashStr = hashlib.sha1(queryStr).hexdigest()
        htqs = 'time=%s&hash=%s' % (currentTime, hashStr)
    
    return htqs

def validateQueryDict(params, timeTolerate, salt):
    hashStr = params.pop('hash')
    queryTime = long(params.pop('time'))
    currentTime = long(time.time())
    if abs(queryTime - currentTime) > long(timeTolerate):
        print 'Time Expire.'
        return False;
    
    queryStr = createHashQueryString(params, salt, queryTime)
    queryDict = getQueryDict(queryStr)
    if not hashStr == queryDict.get('hash'):
        return False
    
    return True 

def getQueryDict(paramStr):
    params = {}
    paramList = paramStr.split('&')
    
    for param in paramList:
        index = param.find('=')
        params.update({param[0:index]:param[(index + 1):len(param)]})
        
    return params

if __name__ == '__main__':
    paramStr = 'performer_id=12478&userid=12478'
    params = getQueryDict(paramStr)
    OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    
    salt = '111'
    currentTime = long(time.time())
    
    currentTime = 1418010963
    params = {'content':'亲爱的'}
    print createHashQueryString(params, salt, currentTime)
