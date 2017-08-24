# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import error
from ..login.models import User
import random
from datetime import datetime


def dashboard(request):
    try:
        if not request.session['id']:
            return redirect('/')
    except:
        return redirect('/')
    
    try:
        if not request.session['alias']:
            return redirect('/')
    except:
        return redirect('/')
         
    context = {
        'users': User.objects.get_users_exclude(request.session['id']),
        'user': User.objects.get_user(request.session['id']),
        'pokers': User.objects.poked_by(request.session['id']),
    }
    
    return render(request, "pokes/dashboard.html", context)

def poke_user(request, poke_id):
    try:
        if not request.session['id']:
            return redirect('/')
    except:
        return redirect('/')
    
    try:
        if not request.session['alias']:
            return redirect('/')
    except:
        return redirect('/')
    
    print "view poke_id: {}".format(poke_id)
    user = User.objects.poke_user(request.session['id'], poke_id)
    return redirect('/pokes')

def poked_by(request):
    try:
        if not request.session['id']:
            return redirect('/')
    except:
        return redirect('/')
    
    try:
        if not request.session['alias']:
            return redirect('/')
    except:
        return redirect('/')
    
    context = {
        'pokers': User.objects.poked_by(request.session['id']),
    }
    return redirect('/pokes', context)

def logout(request):
    del request.session['id']
    del request.session['alias']
    request.session.flush()
    request.session.modified = True
    return redirect('/')