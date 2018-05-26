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
import subprocess, copy, re, clipboard, time, os, datetime, ftplib, glob, sys

# sys.path.append('.')
# sys.path.append('..')

# sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/VIRTUAL/Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects')
from libs_admin import libs
# from Admin_Projects.libs_admin import libs

# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
# 
# from mm.libs_mm import cons_mm, cons_fx, libs, libfx


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

    '''###################
        list of commands
    ###################'''
    lo_Commands = [
        
        ["get_4_Corners", "4 corners of an image file"],
        
        ["???", "unknown"],
    ]
    
    
    # set var
    dic["lo_Commands"] = lo_Commands

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/basics_full.html', dic)

def get_4_corners(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/basics/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/get_4_corners.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/get_4_corners_full.html', dic)

#/ def get_4_corners(request):
#     return render(request, 'ip/basics.html', dic)

#/ def basics(request):