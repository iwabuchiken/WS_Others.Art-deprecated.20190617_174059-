# from django.shortcuts import render
'''###################
    django modules
###################'''
from django.http import HttpResponse
from django.shortcuts import render
from django import template

'''###################
    import : built-in modules        
###################'''
import subprocess, copy, re, clipboard, time, \
        os, datetime, ftplib, glob, sys, cv2 \
        , matplotlib.pyplot as plt

'''###################
    import : orig modules        
###################'''
# sys.path.append('.')
# sys.path.append('..')

# sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/VIRTUAL/Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects')
from libs_admin import libs, lib_ip
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

def get_Corner_Images(img_Src, corner_Length) :
    
    height, width, channels = img_Src.shape
    
    clips = [
    
        img_Src[(height - corner_Length) : height, 0 : corner_Length], # clp_LB
        img_Src[(height - corner_Length) : height, width - corner_Length : width], # clp_RB
        img_Src[0 : corner_Length, 0 : corner_Length], # clp_LU
        img_Src[0 : corner_Length, width - corner_Length : width], # clp_RU
    ]
    
    # return
    return clips
    
#/ def get_Corner_Images(img_RGB, corner_Length) :

def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images, lo_Image_MetaData):
    
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
    
    fname_Log = "get_4_corners.log"
    
    fpath_Log = "%s\\%s" % (dpath_Log, fname_Log)
    
    fout_Log = open(fpath_Log, "a")
    
    # header
    fout_Log.write(
        "[%s %s:%s] =============== Get 4 corners" % \
                (libs.get_TimeLabel_Now(), 
                 os.path.basename(libs.thisfile()), 
                 libs.linenum()))
    
    fout_Log.write("\n")
    
    # iterate
    idxOf_Images = 0
    
    lenOf_LO_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for item in lo_Names_Of_Corner_Images:
    for i in range(lenOf_LO_Names_Of_Corner_Images):
    
        # items
        name = lo_Names_Of_Corner_Images[i]
        
        metaData = lo_Image_MetaData[i]
    
        # file name
        fout_Log.write(name)
#         fout_Log.write(item)
        fout_Log.write('\n')
        
        # meta data
#         print()
#         print("[%s:%d] type(metaData) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData)
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[0]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[0])
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[1]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[1])
#                 ), file=sys.stderr)

                #         max_R
                #         , max_G
                #         , max_B
                #         
                #         , min_R
                #         , min_G
                #         , min_B
                
                #         , valsOf_R
                #         , valsOf_G
                #         , valsOf_B
        
        msg = "R=(%d,%d) G=(%d,%d) B=(%d,%d)" % \
                (metaData[0], metaData[3], metaData[1]
                 , metaData[4], metaData[2], metaData[5]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[6]]
        msg = "\t".join(dat)
#         msg = "\t".join(metaData[6])
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[7]]
        msg = "\t".join(dat)
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[8]]
        msg = "\t".join(dat)
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        
        fout_Log.write('\n')
        
    #/for item in lo_Names_Of_Corner_Images:

    # separator line
    fout_Log.write('\n')
    
    # close file
    fout_Log.close()

    
#/ def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images):
    
def _exec_get_4_corners__Get_MetaData(img_Corners):
    
    # data
    lo_Image_MetaData = []

    for item in img_Corners:
        '''###################
            vars        
        ###################'''
        max_R = -1; max_G = -1; max_B = -1
        min_R = 256; min_G = 256; min_B = 256
    #     min_R = 255; min_G = 255; min_B = 255
    
        # counter
        cntOf_Row = 0
        cntOf_Cell = 0
        
        # values
        valsOf_R = [0] * 256
        valsOf_G = [0] * 256
        valsOf_B = [0] * 256

        for row in item:
        
            for cell in row:
                
#                 #debug
#                 print()
#                 print("[%s:%d] len(cell) => %d" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , len(cell)
#                     ), file=sys.stderr)
#                 return
                
                # get value
                R = cell[0]; G = cell[1]; B = cell[2]
                
                # histogram
                valsOf_R[R] += 1
                valsOf_G[G] += 1
                valsOf_B[B] += 1
                
                # max value
                if R > max_R : max_R = R
                if G > max_G : max_G = G
                if B > max_B : max_B = B
                
                # min value
                if R < min_R : min_R = R
                if G < min_G : min_G = G
                if B < min_B : min_B = B
                
                # count
                cntOf_Cell += 1
            
            # reset count of cells
            cntOf_Cell = 0
            
            # count
            cntOf_Row += 1
            
        #/for row in item:
        
        # append data
        lo_Image_MetaData.append(
            [
#                 valsOf_R
#                 , valsOf_G
#                 , valsOf_B
                
#                 , max_R
                max_R
                , max_G
                , max_B
                
                , min_R
                , min_G
                , min_B
                
                , valsOf_R
                , valsOf_G
                , valsOf_B
                ]
        )
            
    #/for item in img_Corners:
    
    '''###################
        return        
    ###################'''
    #debug
    print()
    print("[%s:%d] len(lo_Image_MetaData) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_Image_MetaData)
                        ), file=sys.stderr)
        
    return lo_Image_MetaData
    
#/ def _exec_get_4_corners__Get_MetaData(img_Corners):

'''==============================================
    _exec_get_4_corners__Get_StatsData(img_Corners)
    
    at : 2018/05/28 07:35:40
    
    @param img_Corners: list of opencv image data (4 corners of a original image)
    
    @return: list of dictionaries
        [{'skew' : 3.032, 'kurtosis' : 1.2230, 'integral' : 3428322},...]
=============================================='''
def _exec_get_4_corners__Get_StatsData(img_Corners):
    
    # data
    lo_Image_StatsData = []
    
    for img_Data in img_Corners:
        
        # var
        do_StasData = {}
        
        print("[%s:%d] getting skew values..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        skew_Values = lib_ip.get_Skews(img_Data)
#         skew = lib_ip.get_Skew(img_Data)
        
        do_StasData['skew_values'] = skew_Values
#         do_StasData['skew'] = skew
        
        # append
        lo_Image_StatsData.append(do_StasData)
        
    #/for img in img_Corners:

    '''###################
        return        
    ###################'''
    return lo_Image_StatsData

#/ def _exec_get_4_corners__Get_StatsData(img_Corners):
    
def _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image):
    
    # count
    cntOf_Corners = 1
    
    
    # time label
    tlabel = libs.get_TimeLabel_Now()

    # paths
    dpath_Plot= "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\img.corners"
    
    lo_Names_Of_Corner_Images = []
    
    for item in img_Corners:

#             xpixels = item.shape[1]
#             ypixels = item.shape[0]
#             
#             dpi = 72
#             scalefactor = 1
# 
#             xinch = xpixels * scalefactor / dpi
#             yinch = ypixels * scalefactor / dpi
#         
#             fig = plt.figure(figsize=(xinch,yinch))
#             
#             plt.imshow(item)
        
#             dpath_Plot= "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\img.corners"
        
        fname_Plot = "img.%s.%s.%d.png" % (tlabel, fname_Image, cntOf_Corners)
#             fname_Plot = "%s.%s.%d.png" % (fname_Image, tlabel, cntOf_Corners)
        
        fpath_Plot = "%s\\%s" % (dpath_Plot, fname_Plot)
        
        # increment
        cntOf_Corners += 1
        
#             plt.savefig(fpath_Plot, dpi=dpi)

#         # cv2 : save image
#         #ref https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/
#         cv2.imwrite(fpath_Plot, item)
        
        #debug
        print()
        print("[%s:%d] fpath_Plot => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Plot
        ), file=sys.stderr)
        
        # append file name
        lo_Names_Of_Corner_Images.append(fname_Plot)
        
#             # reset plot
#             plt.clf()
#             plt.cla()
        
    #/for item in im_Corners:    
    
    '''###################
        return        
    ###################'''
    return lo_Names_Of_Corner_Images
    
#/ def _exec_get_4_corners__SaveImage_4Corners(img_Corners):
    
def exec_get_4_corners(request):
    
    '''###################
        debug
        
        http://127.0.0.1:8001/ip/exec_get_4_corners?dpath_images=C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images&fname_image=IMG_3154.PNG
        
    ###################'''
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    '''###################
        get : params
    ###################'''
    dpath_Images = request.GET.get('dpath_images', False)
    
    fname_Image = request.GET.get('fname_image', False)
    
    '''###################
        get : cv instance        
    ###################'''
    fpath_Image = "%s\\%s" % (dpath_Images, fname_Image)
    
    # validate
    res = os.path.isfile(fpath_Image)
    
    if res == False : #if res == True

        print("[%s:%d] file NOT exist! => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image
        ), file=sys.stderr)
        
        # set dic
        dic['msg'] = "file NOT exist : %s" % fpath_Image
    
    else : #if res == True
    
        print("[%s:%d] file exists => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image
        ), file=sys.stderr)
        
        # cv instance
        img_Orig = cv2.imread(fpath_Image)
        
        print()
        print("[%s:%d] cv2 image ==> loaded" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        
        # convert to RGB
        img_RGB = img_Orig
#         img_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
        
        '''###################
            get : meta data
        ###################'''
        # data
        height, width, channels = img_RGB.shape
        
        print()
        print("[%s:%d] height = %d, width = %d, channels = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , height, width, channels
        ), file=sys.stderr)
        
        '''###################
            get : 4 corners        
        ###################'''
        corner_Length = 280
        
        img_Corners = get_Corner_Images(img_RGB, corner_Length)
        
        print()
        print("[%s:%d] len(img_Corners) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(img_Corners)
        ), file=sys.stderr)
        
        '''###################
            save : images of 4 corners        
        ###################'''
        lo_Names_Of_Corner_Images = \
                _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image)
        
        '''###################
            get : basic data
        ###################'''
        lo_Image_MetaData = _exec_get_4_corners__Get_MetaData(img_Corners)
    
        '''###################
            get : stat data
        ###################'''
        lo_Image_StatsData = _exec_get_4_corners__Get_StatsData(img_Corners)
        
        print()
        print("[%s:%d] lo_Image_StatsData =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        print(lo_Image_StatsData)
        
        '''###################
            write log : file names
        ###################'''
        _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images, lo_Image_MetaData)
        
    #/if res == True
    
    
#     '''###################
#         vars        
#     ###################'''
#     dic = {}

    '''###################
        set : vars
    ###################'''
    dic['dpath_Images'] = dpath_Images
    dic['fname_Image'] = fname_Image
    
    dic['height'] = height
    dic['width'] = width
    dic['channels'] = channels
    
    
    
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