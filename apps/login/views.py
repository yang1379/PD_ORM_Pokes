# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import error
from .models import User
import random
from datetime import datetime


def start(request):

    try:
        request.session['id']
    except:
        request.session['id'] = ""

    try:
        request.session['alias']
    except:
        request.session['alias'] = ''

    return render(request, "login/login.html")

def registration(request):
    
    result = User.objects.validate(request.POST)
#     print result
    if type(result) == dict:
        for field, message in result.iteritems():
            error(request, message, extra_tags=field)

        print "redirect"
        return redirect('/')
    
    request.session['id'] = result.id
    request.session['alias'] = result.alias
    return redirect('/pokes')

def login(request):
    result = User.objects.checkPassword(request.POST)
    if type(result) == dict:
        for field, message in result.iteritems():
            error(request, message, extra_tags=field)
        
            return redirect('/')
    
    request.session['id'] = result.id
    request.session['alias'] = result.alias
    return redirect('/pokes')