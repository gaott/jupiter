# -*- coding: utf-8 -*- 
'''
Created on 2014年10月12日

@author: gaott
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required(login_url='/accounts/login/')
def testTable(request):
    
    abc = '123'
    return render_to_response('test/test_table.html', (request, locals()))