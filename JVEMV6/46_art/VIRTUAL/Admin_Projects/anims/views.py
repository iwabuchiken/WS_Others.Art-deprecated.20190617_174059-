'''###################


data dir
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data
    
###################'''


# from django.shortcuts import render
'''###################
    django modules
###################'''
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from mailbox import fcntl

'''###################
    import : built-in modules        
###################'''
import subprocess, copy, re, clipboard, time, \
        os, datetime, ftplib, glob, sys, cv2 \
        , matplotlib.pyplot as plt, codecs, shutil, numpy as np

'''###################
    import : orig modules        
###################'''
# sys.path.append('.')
# sys.path.append('..')

# sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/VIRTUAL/Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects')
from libs_admin import libs, lib_ip, cons_ip
# from Admin_Projects.libs_admin import libs

# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
# 
# from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    vars : global        
###################'''
numOf_DosAttack = 0

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

#     return render(request, 'ip/index2.html', dic)
#     return render(request, 'ip/index.html', dic)
    return render(request, 'anims/index.html', dic)

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

    return render(request, 'anims/test.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

def _anims__Load_LO_Actions():
    
    dpath_List = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data"

    fname_List = "anims_listof_commands.dat"
    
    fpath_List = os.path.join(dpath_List, fname_List)
    
    f = open(fpath_List, "r")

    # header line
    f.readline()
    
    # body lines
    lines = f.readlines()
    
    # close file
    f.close()
    
    lo_Commands = []
    
    # build list
    for item in lines:

        lo_Commands.append(item.split("\t")[1:])
        
    #/for item in lines:
    
    #debug
    print()
    print("[%s:%d] lo_Commands =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(lo_Commands)
    
    return lo_Commands
    
#/ def _anims__Load_LO_Actions()(request):

def test_OpenCV__NewImage():

    '''###################
        prep        
    ###################'''
    dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
    fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

    '''###################
        prep : image
    ###################'''
    #ref http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
    #ref alpha channel http://opencv.blog.jp/python/alpha_channel
    img = cv2.imread(fpath_Image_File, cv2.IMREAD_UNCHANGED)
    
    print("[%s:%d] img.shape =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(img.shape)
    print()
    
    '''###################
        ops
    ###################'''
    tokens = fname_Image_File.split(".")
    (h, w) = img.shape[:2]
     
    tlabel = libs.get_TimeLabel_Now()

    fname_Dst = "%s.%s.(test_OpenCV__NewImage).%s.%s" \
        % (tokens[0], tokens[1], tlabel, tokens[2])
        
    fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    print("[%s:%d] fname_Dst => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Dst
        ), file=sys.stderr)
    
    '''###################
        image : blank        
    ###################'''
    # blank image
    #ref https://stackoverflow.com/questions/12881926/create-a-new-rgb-opencv-image-using-python
    blank_image = np.zeros((img.shape[0], img.shape[1], 4), np.uint8)
    
    print("[%s:%d] blank_image.shape =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(blank_image.shape)
    
    # shape
    (h2, w2) = blank_image.shape[:2]
    
    # coloring
    # BGRA : A --> 0 for transpanrent
#     blank_image[:, 0 : int(0.5*w2)] = (255, 0, 0, 255)
#     blank_image[:, 0 : int(0.5*w2)] = (100, 100, 100, 200)
#     blank_image[:, 0 : int(0.5*w2)] = (100, 100, 100, 100)
#     blank_image[:, 0 : int(0.5*w2)] = (255,0,0, 0)
#     blank_image[:,0:0.5*w2] = (255,0,0, 0)
#     blank_image[:,0:0.5*width] = (255,0,0, 0)
#     blank_image[:, :] = (255, 0, 0, 0)
#     blank_image[:, :] = (255, 0, 0)

    # copy a partial image of img to blank_image
    cut_height = 120
    cut_width = 120
    
    blank_image[100 : 100 + cut_height, 250 : 250 + cut_width] \
            = img[150:270, 300:420]
#     blank_image[150:270, 300:420] = img[150:270, 300:420]
    
    
    #write
    cv2.imwrite(fpath_Dst, blank_image)
#     cv2.imwrite(fpath_Dst, mask)
    
#     #ref https://stackoverflow.com/questions/48384516/python-opencv-cropping-images-and-isolating-specific-objects
#     mask = np.zeros(img.shape[:2],np.uint8)
#     
#     print()
#     print("[%s:%d] mask[0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(mask[0])
#                 ), file=sys.stderr)
#     print(mask[0])
#     
#     print()
#     print("[%s:%d] img[0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(img[0])
#                 ), file=sys.stderr)
#     print(img[0])
#     
#     print()
#     print("[%s:%d] img[0][0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(img[0][0])
#                 ), file=sys.stderr)
#     print(img[0][0])
    
#     print()
#     print("[%s:%d] mask[0][0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(mask[0][0])
#                 ), file=sys.stderr)
#     print(mask[0][0])
    
#     print("[%s:%d] mask.shape[0] = %d, mask.shape[1] = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , mask.shape[0], mask.shape[1]
#                 ), file=sys.stderr)
#     
#     for i in range(0, mask.shape[0]):   # height
#         for j in range(0, mask.shape[1]):   # width
#          
#             mask[i][j][0] = 255
#             mask[i][j][1] = 0
#             mask[i][j][2] = 0
#              
#         #/for i in range(0, mask.shape[0]:
# 
#     #write
#     cv2.imwrite(fpath_Dst, mask)


#/ def test_OpenCV__NewImage():
    
def _anims_JS__1_Move_Leaves__Test_1_Resize__exec(angle, scale, img, center, fpath_Dst):
    
#     angle_45 = 45
#     scale = 1.0

    (h, w) = img.shape[:2]
#     center = (365, 203)
#     center = (w / 2, h / 2)
    
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (h, w))
    
#     tokens = fname_Image_File.split(".")
#     fname_Dst = "%s.%s.(rotate=%d).%s.%s" \
#             % (tokens[0], tokens[1], angle_45, libs.get_TimeLabel_Now(), tokens[2])
    
#     fpath_Image_File__Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    cv2.imwrite(fpath_Dst, rotated)
    
#/ def _anims_JS__1_Move_Leaves__Test_1_Resize__exec():
    
def _anims_JS__1_Move_Leaves__Test_1_Resize(request):

    '''###################
        prep        
    ###################'''
    dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
    fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

    '''###################
        prep : params
            main.js :: _anims_Action_LinkTo__1(_param)
            , option_tick_move_X : _option_tick_move_X
            , option_tick_move_Y : _option_tick_move_Y
            
            , opt_rotate_Start : _opt_rotate_Start
            , opt_rotate_End : _opt_rotate_End

    ###################'''
    param_Loc_Start_X = request.GET.get('option_loc_start_X', False)
    param_Loc_Start_Y = request.GET.get('option_loc_start_Y', False)
    
    param_Cut_Width = request.GET.get('opt_cut_width', False)
    param_Cut_Height = request.GET.get('opt_cut_height', False)
    
    # modify
    # ref tertiary https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
    param_Loc_Start_X = 0 if (param_Loc_Start_X == False) else int(param_Loc_Start_X)
    param_Loc_Start_Y = 0 if (param_Loc_Start_Y == False) else int(param_Loc_Start_Y)
    
    param_Cut_Width = 100 if (param_Cut_Width == False) else int(param_Cut_Width)
    param_Cut_Height = 100 if (param_Cut_Height == False) else int(param_Cut_Height)
    
    
    print("[%s:%d] param_Cut_Width = %d, param_Cut_Height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param_Cut_Width, param_Cut_Height
            ), file=sys.stderr)
    
#     print("[%s:%d] param_Loc_Start_X = %d, param_Loc_Start_Y = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , param_Loc_Start_X, param_Loc_Start_Y
#         ), file=sys.stderr)
    
    '''###################
        op        
    ###################'''
    '''###################
        img : read
    ###################'''
    #ref http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
    #ref alpha channel http://opencv.blog.jp/python/alpha_channel
    img = cv2.imread(fpath_Image_File, cv2.IMREAD_UNCHANGED)
#     img = cv2.imread(fpath_Image_File)
#     img = cv2.imread(fpath_Image_File, cv2.IMREAD_COLOR)
    
#     orgHeight, orgWidth = img.shape[:2]
#     size = (int(orgWidth/2), int(orgHeight/2))
# #     size = (int(orgHeight/2), int(orgWidth/2))
#     
# #     size = (orgHeight/2, orgWidth/2)
#     
#     halfImg = cv2.resize(img, size)
#     
#     tokens = fname_Image_File.split(".")
#     fname_Half = "%s.%s.(half).%s.%s" \
#             % (tokens[0], tokens[1], libs.get_TimeLabel_Now(), tokens[2])
# 
#     cv2.imwrite(os.path.join(dpath_Image_File, fname_Half), halfImg)
#     cv2.imwrite('half.jpg', halfImg)
    
    '''###################
        rotate        
    ###################'''
    #abcde
    tokens = fname_Image_File.split(".")
    (h, w) = img.shape[:2]
     
    tlabel = libs.get_TimeLabel_Now()
#     
#     for i in range(0, 10):
# #     for i in range(0, 5):
#         
#         angle = i * 5
#         scale = 1.0
#         
#         #ref radians https://docs.scipy.org/doc/numpy/reference/generated/numpy.radians.html
#         span = int((370 - w / 2) * np.sin(np.radians(angle)))
#         span_w = int((370 - w / 2) * np.cos(np.radians(angle)))
#         
#         center = (w / 2 + span_w, h / 2 + span)
# #         center = (w / 2, h / 2 + span)
# #         center = (w / 2, h / 2 - span)
# #         (h, w) = img.shape[:2]
# #         center = (w / 2, h / 2)
#     
#         fname_Dst = "%s.%s.(rotate=%d).%s.(center=%d,%d).%s" \
#                 % (tokens[0], tokens[1], angle, tlabel, center[0], center[1], tokens[2])
# #                 % (tokens[0], tokens[1], angle, tlabel, tokens[2])
# #                 % (tokens[0], tokens[1], angle, libs.get_TimeLabel_Now(), tokens[2])
#          
#         fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
#         
#         _anims_JS__1_Move_Leaves__Test_1_Resize__exec(angle, scale, img, center, fpath_Dst)
#         
#         
#     #/for i in range(0, 10):

    '''###################
        move image        
    ###################'''
    #ref https://stackoverflow.com/questions/23464495/fastest-way-to-move-image-in-opencv
    fname_Dst = "%s.%s.(moved).%s.%s" \
        % (tokens[0], tokens[1], tlabel, tokens[2])
        
    fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    print("[%s:%d] fname_Dst => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Dst
        ), file=sys.stderr)
    
    img_Partial = img[
                param_Loc_Start_Y : param_Loc_Start_Y + param_Cut_Height
                , param_Loc_Start_X : param_Loc_Start_X + param_Cut_Width
                
                ]  # h, w
#     img_Partial = img[param_Loc_Start_Y : 270, param_Loc_Start_X : 420]  # h, w
#     img_Partial = img[150 : 270, 300 : 420]  # h, w
#     img_Partial = img[0 : 100, 0 : 50]  # h, w
#     img_Partial = img[cv2.Rect(0, 0, 100, 100)]
#     img_Partial = img(cv2.Rect(0, 0, 100, 100))
    
    cv2.imwrite(fpath_Dst, img_Partial)
#     cv2.imwrite(fname_Dst, img_Partial)
    
    
#     #ref https://www.tutorialkart.com/opencv/python/opencv-python-rotate-image/#opencv-python-rotate-image
#     angle_45 = 45
#     scale = 1.0

#     (h, w) = img.shape[:2]
#     center = (365, 203)
# #     center = (w / 2, h / 2)
#     
#     M = cv2.getRotationMatrix2D(center, angle_45, scale)
#     rotated_45 = cv2.warpAffine(img, M, (h, w))
# #     rotated90 = cv2.warpAffine(img, M, (h, w))
#     
#     tokens = fname_Image_File.split(".")
#     fname_Dst = "%s.%s.(rotate=%d).%s.%s" \
#             % (tokens[0], tokens[1], angle_45, libs.get_TimeLabel_Now(), tokens[2])
#     
#     fpath_Image_File__Dst = os.path.join(dpath_Image_File, fname_Dst)
#     
#     cv2.imwrite(fpath_Image_File__Dst, rotated_45)
    
    
#/ def _anims_JS__1_Move_Leaves__Test_1_Resize():
    
def _anims_JS__1_Move_Leaves(request):
    
    '''###################
        tests
    ###################'''
    test_OpenCV__NewImage()
    
    '''###################
        ops
    ###################'''
#     _anims_JS__1_Move_Leaves__Test_1_Resize(request)
    
    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "OK"
    
    return (status, msg)
    
#/ def _anims_JS__1_Move_Leaves(request):
    
def anims_JS(request):
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    dic = {
        
        "message" : ""
        , "message_2" : ""
        }
    
    render_Page = 'anims/anims/plain_anims.html'
    
    '''###################
        params
    ###################'''
    param = request.GET.get('param', False)
    
    #debug
#     print("[%s:%d] param => %s" % \
    print("[%s:%d] param => %s ============================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param
            ), file=sys.stderr)

    '''###################
        dispatch
    ###################'''
    if param == cons_ip.Anims_Params.PARAM__1_MOVE_LEAVES.value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM__1_MOVE_LEAVES        
        ###################'''
        # call func
        (status, msg) = _anims_JS__1_Move_Leaves(request)

        dic['message'] += "move leaves"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start

    dic['message_2'] += "(time = %s) (elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)


    '''###################
        render
    ###################'''
    return render(request, render_Page, dic)
    
    
#/ def anims_JS(request):
    
    
def anims(request):
    
    now = datetime.datetime.now()


    action = "anims"
    message = "yes"

    page_Title = "IP / anims"

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
    lo_Commands = _anims__Load_LO_Actions()
#     lo_Commands = [
#          
#         ["move_leaves", "image sequence for moving leaves"],
#          
#         ["???", "unknown"],
#     ]
     
     
    # set var
    dic["lo_Commands"] = lo_Commands
    
    dic["count"] = 0

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
    
        return render(request, 'anims/anims/anims.html', dic)
#         return render(request, 'ip/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'anims/anims/anims_full.html', dic)
#         return render(request, 'ip/basics_full.html', dic)
#/ def basics(request):

def open_dir(request):
    
    '''###################
        params
    ###################'''
    param = request.GET.get('param', False)
    
    print("[%s:%d] param => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , param
        ), file=sys.stderr)
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    print()
    print("[%s:%d] opening dir..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    '''###################
        build : command string        
    ###################'''
    command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\utils\\open_anims_log_dir.bat"
#     command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\utils\\open_anims_log_dir.bat"

    cmd_Full = [command]  #=> 

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

    '''###################
        render
    ###################'''
    return render(request, 'anims/anims/plain_anims.html', dic)
    
#/ def open_image_dir(request):

