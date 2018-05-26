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
        get : files list
    ###################'''
    dpath_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\images"
    
    fpath_Glob = "%s\\*" % (dpath_Images)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)

    lo_Files.sort()


    # set list
    dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
    
    # set : dpath
    dic['dpath_Images'] = dpath_Images
    
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

def exec_get_4_corners(request):
    
    '''###################
        get : params
    ###################'''
    dpath_Images = request.GET.get('dpath_images', False)
    
    fname_Image = request.GET.get('fname_image', False)
    
    '''###################
        vars        
    ###################'''
    dic = {}

    '''###################
        set : vars
    ###################'''
    dic['dpath_Images'] = dpath_Images
    dic['fname_Image'] = fname_Image
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/get_4_corners/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/exec_get_4_corners.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/exec_get_4_corners_full.html', dic)

#/ def exec_get_4_corners(request):
#     return render(request, 'ip/basics.html', dic)

#/ def basics(request):

def open_image_dir(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    print()
    print("[%s:%d] opening image dir..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    '''###################
        build : command string        
    ###################'''
    command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\utils\\open_image_dir.bat"
#     command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\images"
#     command = "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images"
#     command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)

#     print()
#     print("[%s:%d] _im_actions__Ops_13()" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)

    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    print()
    print("[%s:%d] command => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , command
            ), file=sys.stderr)

    '''###################
        subprocess        
    ###################'''
    #ref https://stackoverflow.com/questions/13525882/tasklist-output answered Nov 23 '12 at 9:36
    res = subprocess.call(cmd_Full)
#     res = subprocess.check_output(cmd_Full)



    return render(request, 'ip/open_image_dir.html', dic)

    
#/ def open_image_dir(request):