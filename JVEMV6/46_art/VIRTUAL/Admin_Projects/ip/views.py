# from django.shortcuts import render
'''###################
    django modules
###################'''
from django.http import HttpResponse
from django.shortcuts import render
from django import template

'''###################
    built-in modules        
###################'''
import subprocess, copy, re, clipboard, time, os, datetime, ftplib, glob

# Create your views here.
# def index():
def index(request):
    
    now = datetime.datetime.now()


    action = "index"
    message = "yes"

    page_Title = "Image Processing"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    return render(request, 'ip/index.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

def test(request):
    
    now = datetime.datetime.now()


    action = "test"
    message = "yes"

    page_Title = "Image Processing"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    return render(request, 'ip/test.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

def basics(request):
    
    now = datetime.datetime.now()


    action = "basics"
    message = "yes"

    page_Title = "IP / basics"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    return render(request, 'ip/basics.html', dic)

#/ def basics(request):