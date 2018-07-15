# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\6_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
at : 2018/07/15 08:09:48

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops
python 6_1.py
python 6_1.py -s1.0

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''
###############################################
import sys, cv2
# from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
from win32api import GetSystemMetrics
from matplotlib import pylab as plt

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
    
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    if event == cv2.EVENT_LBUTTONDOWN:
        
        refPt = [(x, y)]
        
        print()
        print("[%s:%d] EVENT_LBUTTONDOWN (x = %d / y = %d)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , x, y
                ), file=sys.stderr)
#     print()
#     print("[%s:%d] x = %d, y = %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , x, y
#             ), file=sys.stderr)
    
#/ def click_and_crop(event, x, y, flags, param):

'''###################
    get_RGB_Vals      
    
    from : test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub)
    at : 2018/07/15 08:17:58
    
    @return: list of RGB vals
            e.g. [156, 167, 153,...], [156, 167, 153,...], [156, 167, 153,...]
    
###################'''
def get_RGB_Vals(img_Sub):
    
    '''###################
        message        
    ###################'''
    cntOf_Rows = 0
    
    lo_Rs = []
    lo_Gs = []
    lo_Bs = []
    
    for row in img_Sub:
        
        # counter
        cntOf_Rows += 1
        
        for cell in row:
    
            '''###################
                append        
            ###################'''
            lo_Rs.append(cell[0])
            lo_Gs.append(cell[1])
            lo_Bs.append(cell[2])
            
        #/for cell in row:
        
    #/for row in img_Sub:
    
    '''###################
        return        
    ###################'''
    return lo_Rs, lo_Gs, lo_Bs

#/ def test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub):

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

#/ def test_7__SubImage_RGB_Vals__Get_Scaling():

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

def __test_1__Set_Starting_Point__Plotting(lo_Rs, lo_Gs, lo_Bs, dpath_Ops_Images):
    
    y_pos = np.arange(len(lo_Rs))

    performance = lo_Rs
    
    #ref https://stackoverflow.com/questions/21254472/multiple-plot-in-one-figure-in-python
    plt.plot(y_pos, lo_Rs, 'r-', label='lo_Rs')
    plt.plot(y_pos, lo_Gs, 'g-', label='lo_Gs')
    plt.plot(y_pos, lo_Bs, 'b-', label='lo_Bs')
    
    plt.legend(loc='best')
    
    ax = plt.gca()
     
    #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
    ax.grid(which='major', axis='both', linestyle='--')
    ax.grid(which='minor', axis='both', linestyle='--')
 
    ax.set(aspect=1,
           xlim=(0, len(lo_Rs)),
           ylim=(140, 250))
    
    fpath_Save_Image = os.path.join(dpath_Ops_Images, "plot_" + libs.get_TimeLabel_Now() + ".png")
    
    
    result = plt.savefig(fpath_Save_Image)
    
    print("[%s:%d] save fig => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , result, fpath_Save_Image
        ), file=sys.stderr)
#/ def __test_1__Set_Starting_Point__Plotting():

def __test_1__Set_Starting_Point__Key_Inputs():
    
    while True :
        
        k = cv2.waitKey(0) & 0xFF
    
        #ref https://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html
        if k == ord('q'):
            
            break
        
        else:
            
            print("[%s:%d] waitKey => %d (%s) (press 'q' to quit)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , k, str(chr(k))
#                 , k, str(unichr(k))
                ), file=sys.stderr)
            
            
#     while True :

    print("[%s:%d] waitKey => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , k
        ), file=sys.stderr)

#/ def __test_1__Set_Starting_Point__Key_Inputs:

def __test_1__Set_Starting_Point__Window_Ops(args, width, height, img_Sub):
    
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
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_Sub)
#     cv2.imshow('window', img_ForDisp)
    
    print("[%s:%d] waiting for key(0)....." % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return win_Resize_Width, win_Resize_Height, scr_W, scr_H
    
#/ def __test_1__Set_Starting_Point__Window_Ops():

def test_1__Set_Starting_Point():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1__Set_Starting_Point =======================" % \
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
        sub image        
    ###################'''
    # height, width
    img_Sub = img_ForDisp[19:69, 245:246]
#     img_Sub = img_ForDisp[19:186, 245:246]
    
    # meta data
    height_Sub, width_Sub, channels_Sub = img_Sub.shape
    
    print("[%s:%d] width_Sub = %d, height_Sub = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , width_Sub, height_Sub
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] img_Sub[0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0])
    print("[%s:%d] img_Sub[0][0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0][0])
    
    '''###################
        get : RGB vals        
    ###################'''
    lo_Rs, lo_Gs, lo_Bs = get_RGB_Vals(img_Sub)
#     lo_Rs, lo_Gs, lo_Bs = test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub)
    
#     print()
#     print("[%s:%d] lo_Rs =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                
#                 ), file=sys.stderr)
#     print(lo_Rs)
    
    '''###################
        plot        
    ###################'''
#     yax_vals = [200, 100,0]
#     plt.bar(yax_vals, lo_Rs)
# #     plt.bar(lo_Rs, yax_vals)
# #     plt.bar(lo_Rs)
# #     plt.plot(lo_Rs)
#     
#     plt.show()
    
    __test_1__Set_Starting_Point__Plotting(lo_Rs, lo_Gs, lo_Bs, dpath_Ops_Images)
#     y_pos = np.arange(len(lo_Rs))
# 
#     performance = lo_Rs
#     
#     #ref https://stackoverflow.com/questions/21254472/multiple-plot-in-one-figure-in-python
#     plt.plot(y_pos, lo_Rs, 'r-', label='lo_Rs')
#     plt.plot(y_pos, lo_Gs, 'g-', label='lo_Gs')
#     plt.plot(y_pos, lo_Bs, 'b-', label='lo_Bs')
#     
#     plt.legend(loc='best')
#     
#     ax = plt.gca()
#      
#     #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(which='major', axis='both', linestyle='--')
#     ax.grid(which='minor', axis='both', linestyle='--')
#  
#     ax.set(aspect=1,
#            xlim=(0, len(lo_Rs)),
#            ylim=(140, 250))
#     
#     fpath_Save_Image = os.path.join(dpath_Ops_Images, "plot_" + libs.get_TimeLabel_Now() + ".png")
#     
#     
#     result = plt.savefig(fpath_Save_Image)
#     
#     print("[%s:%d] save fig => %s (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , result, fpath_Save_Image
#         ), file=sys.stderr)
    
#     plt.show()
#     
#     debug
#     return
    
    '''######################################
        prep : window
    ######################################'''

    win_Resize_Width, win_Resize_Height, scr_W, scr_H = \
                __test_1__Set_Starting_Point__Window_Ops(args, width, height, img_Sub)
#     window_1 = "window"
#     
#     #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
#     #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
#     cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
#     
#     '''###################
#         get : scaling        
#     ###################'''
#     scaling = get_Scaling(args)
# #     scaling = test_7__SubImage_RGB_Vals__Get_Scaling(args)
#     
#     win_Resize_Height = math.floor(scaling * height)
#     win_Resize_Width = math.floor(scaling * width)
#     
#     # validate
#     scr_W = GetSystemMetrics(0)
#     scr_H = GetSystemMetrics(1)
#     
#     '''###################
#         resize image        
#     ###################'''
#     win_Resize_Width, win_Resize_Height = resize_Image(width, height, scaling, scr_W, scr_H)
# #     win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)
# 
#     '''###################
#         disp : image
#     ###################'''
#     cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
#     
#     '''###################
#         mouse events
#     ###################'''
#     '''###################
#         mouse events
#     ###################'''
#     #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
#     cv2.setMouseCallback(window_1, click_and_crop)
# #     cv2.setMouseCallback("image", click_and_crop)
#         
#     '''###################
#         show
#     ###################'''
# 
#     cv2.imshow('window', img_Sub)
# #     cv2.imshow('window', img_ForDisp)
#     
#     print("[%s:%d] waiting for key(0)....." % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
    
#     k = cv2.waitKey(0) & 0xFF
    
    '''###################
        key inputs        
    ###################'''
    __test_1__Set_Starting_Point__Key_Inputs()
    
    
#     while True :
#         
#         k = cv2.waitKey(0) & 0xFF
#     
#         #ref https://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html
#         if k == ord('q'):
#             
#             break
#         
#         else:
#             
#             print("[%s:%d] waitKey => %d (%s) (press 'q' to quit)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , k, str(chr(k))
# #                 , k, str(unichr(k))
#                 ), file=sys.stderr)
#             
#             
# #     while True :
# 
#     print("[%s:%d] waitKey => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , k
#         ), file=sys.stderr)

#     result = cv2.waitKey(0)
    
#     print("[%s:%d] result => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , result
#         ), file=sys.stderr)
    
    '''###################
        window : close        
    ###################'''
    cv2.destroyAllWindows()
    
#/ def test_5():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
#     test_8__Matplotlib__Bar_Chart()
    
    test_1__Set_Starting_Point()
    
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
