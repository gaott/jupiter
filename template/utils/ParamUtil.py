#encoding=utf-8
'''
Created on 2013-7-23

@author: gaott
'''
import urllib


def getParamDict(paramStr):
    params = {}
    paramList = paramStr.split('&')
    
    for param in paramList:
        listAppVersion = param.find('=')
        params.update({param[0:listAppVersion]:param[(listAppVersion + 1):len(param)]})
        
    return params

def decodeParam(param):
    param = urllib.unquote(str(param)).decode('utf8')
    return param.encode('utf-8')

if __name__ == '__main__':
    a = 'a=11&b=222'
    print getParamDict(a)