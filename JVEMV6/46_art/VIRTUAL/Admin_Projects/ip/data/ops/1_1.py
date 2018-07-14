# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\sounds\mp3\1_1.py
at : 2018/06/30 09:32:18

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops
python 1_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''
###############################################
import sys, cv2
# from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
from win32api import GetSystemMetrics

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
import os, glob, getopt, math as math
# import inspect

# import math as math

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

'''###################
    click_and_crop(event, x, y, flags, param)
    
    at : 2018/06/30 09:53:22
    
###################'''
#ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
def click_and_crop(event, x, y, flags, param):
    
    print()
    print("[%s:%d] x = %d, y = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , x, y
            ), file=sys.stderr)
    
#/ def click_and_crop(event, x, y, flags, param):

'''###################
    test_5()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
def test_5():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_4 =======================" % \
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
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
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
#                 scaling = item[1]
                
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
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    if win_Resize_Width > scr_W : win_Resize_Width = scr_W
    if win_Resize_Height > scr_H : win_Resize_Width = scr_H
    
    #debug
    print("[%s:%d] win_Resize_Width = %.03f, win_Resize_Height = %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , win_Resize_Width, win_Resize_Height
                    ), file=sys.stderr)
    print()
    
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_ForDisp)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#/ def test_5():

'''###################
    test_4()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
def test_4():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_4 =======================" % \
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
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
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
#                 scaling = item[1]
                
                break
                
            #/if item.startswith("-s")
    
    
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    
    
#     scaling = 0.5
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    if win_Resize_Width > scr_W : win_Resize_Width = scr_W
    if win_Resize_Height > scr_H : win_Resize_Width = scr_H
    
        
        
    
    #debug
    print("[%s:%d] win_Resize_Width = %.03f, win_Resize_Height = %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , win_Resize_Width, win_Resize_Height
                    ), file=sys.stderr)
    print()
    
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
#     cv2.resizeWindow(window_1, 600,600)
    
#     cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_ForDisp)
#     cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():


def test_3():

#     '''###################
#         get : args        
#     ###################'''
    lib_ip.test__get_Opt_IP()
	#ref https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python answered Oct 27 '10 at 13:27
#     args = sys.argv
#     
#     print()
#     print("[%s:%d] args =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(args)

#/ def test_3():

'''###################
    test_2()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        
        <quit program>
        return key
    
###################'''
def test_2():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_2 =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)

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
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    scaling = 0.5
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
#     cv2.resizeWindow(window_1, 600,600)
    
#     cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_ForDisp)
#     cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():

def test_1():

    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    # meta data
    height, width, channels = img_Orig.shape
    
    '''######################################
        show : image
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
    
    

        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_4()
#     test_2()
#     test_3()
#     test_2()
#     test_1()
    
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
