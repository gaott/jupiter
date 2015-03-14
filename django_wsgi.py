# -*- coding: utf-8 -*-  
'''
Created on 2014年7月5日

@author: gtt
'''

import os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'template.settings'
application = django.core.handlers.wsgi.WSGIHandler()

#初始化数据库链接
#from template.StartUp import start
#start()