# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\10_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\6_1.py
at : 2018/07/28 10:48:35

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops
python 10_1.py -s1.0
python 6_1.py -s1.0

python 6_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

20180721_111655
C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images\
'''
###############################################
import sys, cv2
# from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
from win32api import GetSystemMetrics
from matplotlib import pylab as plt
from copy import deepcopy

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects') # libs_mm

from libs_admin import libs, lib_ip

'''###################
    import : built-in modules        
###################'''
# import getopt
import os, glob, getopt, math as math, numpy as np
# import inspect

'''###################
    constants : global        
###################'''
# import math as math
refPt_Start = [-1] * 2
refPt_End = [-1] * 2
# refPt_Start = []
# refPt_End = []

flg_Set_Points  = ""
flg_Get_RGB_Vals  = False

POINTS_START    = "START"
POINTS_END      = "END"
POINTS_NEUTRAL  = "NEUTRAL"

KEY_INPUTS__END    = 'e'
KEY_INPUTS__RGB    = 'g'
KEY_INPUTS__HELP    = 'h'
KEY_INPUTS__QUIT    = 'q'
KEY_INPUTS__RESET    = 'r'
KEY_INPUTS__START    = 's'
KEY_INPUTS__EXECUTE    = 'x'

DPATH_IMAGE_OUTPUT = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"

###############################################
# def show_Message() :
#     
#     msg = '''
#     <Options>
#     -v	Volume down the amplitude --> 1.0 * v / 1000
#     -f	Base frequency ---> e.g. 262 for the A tone
#     -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
#     
#     print (msg)

def show_Message():

#     print("'q' to quit")
#     print("'x' to execute")
#     print("'h' to show this key list")
    print("'g'\tset flag for getting RGB values")
    print("'h'\tshow this key list")
    print("'q'\tquit")
    print("'r'\treset start/end")
    print("'x'\texecute")
#             print("'e' to execute")
#             print("left click ==> set the starting point")
#             print("right click ==> set the ending point")
    print("'s' then left click ==> set the starting point")
    print("'e' then right click ==> set the ending point")
    print()

#/ def show_Message():

'''###################
    resize_Image()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
# def test_5__Resize_Image(width, height, scaling, scr_W, scr_H):
def resize_Image(width, height, scaling, scr_W, scr_H):
    
    q1 = 1.0 * width / height

    s = scaling
    
    flg_WorH = ""
    
    # j1
    if s >= 0 : #if s >= 0
            
        ### j1 : p1
        A = 0
        
        if width >= height : #if width > height
            
                flg_WorH = "width"
                
                A = width
            
        else : #if width > height
        
            flg_WorH = "height"
        
            A = height
            
        #/if width > height
        
        ### j1 : p2
        m = A * s
        
        print("[%s:%d] m => %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , m
                ), file=sys.stderr)
        
        ### j1 : p3
        Z = 0
        
        if flg_WorH == "width" : #if flg_WorH == "width"
            
            Z = scr_W
            
        else : #if flg_WorH == "width"
        
            Z = scr_H
        
        #/if flg_WorH == "width"
        
        ### j2
        result = (m > Z)

        '''###################
            vars
        ###################'''
        win_Resize_Height = 0
        win_Resize_Width = 0
        
        if result == True : #if result == True

            print("[%s:%d] m > Z : m = %.03f, Z = %d, flg_WorH = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , m, Z, flg_WorH
                ), file=sys.stderr)
            
            ### j2 : p1
            q2 = 1.0 * Z / A
            
            print("[%s:%d] q2 => %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , q2
                    ), file=sys.stderr)

            '''###################
                calc
            ###################'''
            win_Resize_Height = math.floor(height * q2)
            win_Resize_Width = math.floor(width * q2)
#             win_Resize_Height = int(height * q2)
#             win_Resize_Width = int(width * q2)
#             win_Resize_Height = height * q2
#             win_Resize_Width = width * q2
            
        else : #if result == True
        
            print("[%s:%d] m <= Z" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
            
        
            '''###################
                calc
            ###################'''
            win_Resize_Height = math.floor(scaling * height)
            win_Resize_Width = math.floor(scaling * width)

        
        #/if result == True
        
    else : #if s >= 0
    
        '''###################
            calc
        ###################'''
        win_Resize_Height = math.floor(scaling * height)
        win_Resize_Width = math.floor(scaling * width)
    
    #/if s >= 0

#     '''###################
#         calc
#     ###################'''
#     win_Resize_Height = math.floor(scaling * height)
#     win_Resize_Width = math.floor(scaling * width)

    '''###################
        return        
    ###################'''
    #debug
    print("[%s:%d] win_Resize_Width = %d, win_Resize_Height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , win_Resize_Width, win_Resize_Height
            ), file=sys.stderr)
    print()
    
    return win_Resize_Width, win_Resize_Height
    
#/ def test_5():

'''###################
    get_Scaling        
    
    from : test_7__SubImage_RGB_Vals__Get_Scaling(args)
    at : 2018/07/15 08:22:52
    
###################'''
def get_Scaling(args):
    
    # scaling
    scaling = 1.0
    
#     #debug
#     print("[%s:%d] args =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     print(args)
    
    if len(args) > 0 : #if len(args) > 1
    
        optlist, args = getopt.getopt(args, "s:")
        
        print("[%s:%d] optlist =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(optlist)
        
        for item in optlist:
            
            #debug
            print("[%s:%d] item =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
            print(item)
    
            if item[0].startswith("-s") : #if item.startswith("-s")
    
                scaling = float(item[1])
                
                break
                
            #/if item.startswith("-s")
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return scaling


def __test_1__Color_Filtering__Window_Ops(args, width, height, img_ForDisp):
    
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    '''###################
        get : scaling        
    ###################'''
    scaling = get_Scaling(args)
#     scaling = test_7__SubImage_RGB_Vals__Get_Scaling(args)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    '''###################
        resize image        
    ###################'''
    win_Resize_Width, win_Resize_Height = resize_Image(width, height, scaling, scr_W, scr_H)
#     win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)

    '''###################
        disp : image
    ###################'''
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
    
    '''###################
        mouse events
    ###################'''
    '''###################
        mouse events
    ###################'''
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_ForDisp)
# def __test_1__Color_Filtering__Window_Ops():

def __test_1__Color_Filtering__Exec_Filtering(img_ForDisp):
    
    img_Copy = deepcopy(img_ForDisp)
    
    '''###################
        process partial        
    ###################'''
    time_Label = libs.get_TimeLabel_Now()
    
    # horizontal
    x1 = 100
    x2 = 400
    
    # vertical
    y1 = 100
    y2 = 550
#     y2 = 150
    
    # image : orig
    fname = "img_ForDisp_%s.%d-%d_%d-%d.png" \
            % (time_Label
               , x1, x2
               , y1, y2
               )
      
    fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
    
    result = cv2.imwrite(fpath_Save_Image, img_ForDisp)
    
    print("[%s:%d] image ==> saved : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , fpath_Save_Image
                    ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] img_Copy[y1 = %d][x1 = %d]" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , y1, x1
        ), file=sys.stderr)
    print(img_Copy[y1][x1])
    
    # image : copy 
#     leOf_Rows = len(img_Copy) 
    
    '''###################
        filtering        
    ###################'''
    pixel_Target = img_Copy[y1][x1]
    
    threshold_Diff = 10
    
    for i in range(y1, y2):
#     for i in range(100, 200):
#     for i in range(100, lenOf_Rows):
            
        row = img_Copy[i]
        
        for j in range(x1, x2):
#         for j in range(100, 200):
#         for pixel in row:
            
            pixel = row[j]
            
            if pixel[0] < (pixel_Target[0] - threshold_Diff) \
                and pixel[1] < (pixel_Target[1] - threshold_Diff) \
                and pixel[2] < (pixel_Target[2] - threshold_Diff) : 
                
                    pixel[0] = 255
                    pixel[1] = 255
                    pixel[2] = 255
            
#             if pixel[0] < (pixel_Target[0] - threshold_Diff) : pixel[0] = 255
#             if pixel[1] < (pixel_Target[1] - threshold_Diff) : pixel[1] = 255
#             if pixel[2] < (pixel_Target[2] - threshold_Diff) : pixel[2] = 255
                
            #/if pixel[0] < (pixel_Target[0] - threshold_Diff)
        
        
#             pixel[0] = 0
#             pixel[1] = 0
#             pixel[2] = 0
            
        #/for pixel in row:

    #/for row in img_Copy:

    fname = "img_Copy_%s.%d-%d_%d-%d.png" \
            % (time_Label
               , x1, x2
               , y1, y2
               )
    
    fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
      
    #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    result = cv2.imwrite(fpath_Save_Image, img_Copy)
    
    print("[%s:%d] image ==> saved : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , fpath_Save_Image
                    ), file=sys.stderr)
    
#/ def __test_1__Color_Filtering__Exec_Filtering(img_ForDisp):

def test_1__Color_Filtering():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1__Color_Filtering =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)
    
    '''######################################
        get : args
    ##################
    ####################'''
    args = sys.argv[1:]
#     args = sys.argv
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    #debug
    print("[%s:%d] source image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Ops_Image
            ), file=sys.stderr)
    
    print("[%s:%d] width = %d, height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , width, height
            ), file=sys.stderr)
    
    '''###################
        show image        
    ###################'''
#     __test_1__Color_Filtering__Window_Ops(args, width, height, img_ForDisp)
    
    '''###################
        filtering
    ###################'''
    __test_1__Color_Filtering__Exec_Filtering(img_ForDisp)
    
    '''###################
        window : close        
    ###################'''
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
#/ def test_5():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1__Color_Filtering()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

'''
<usage>
test_1.py [-fXXX]  #=> frequency
test_1.py -f402
'''
if __name__ == "__main__" :

    '''###################
    	validate : help option		
    ###################'''

    '''###################
    	get options		
    ###################'''

    '''###################
    	evecute		
    ###################'''
    exec_prog()

    print()
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
