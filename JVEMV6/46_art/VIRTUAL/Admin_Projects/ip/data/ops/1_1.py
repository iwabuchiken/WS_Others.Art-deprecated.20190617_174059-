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

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects') # libs_mm

from libs_admin import libs

'''###################
    import : built-in modules        
###################'''
# import getopt
import os, glob
# import inspect

import math as math

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
#     test_2()
    test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print ("[%s:%d] exec_prog" % (thisfile(), linenum()))
    
#     #debug
#     return
    
    
#     A = 1     #振幅
#     fs = 16000 #サンプリング周波数
# #     fs = 8000 #サンプリング周波数
#     f0 = 392  #周波数
# #     f0 = 262  #周波数
# #     f0 = 440  #周波数
#     sec = 5   #秒
#     
#     phase_Param = 4
#     
#     phase = f0 * (phase_Param / 2)
# #     phase = f0 * (4 / 2)
# #     phase = f0 / 2
#     
#     # bin data
#     binwave = gen_WaveData(fs, f0, phase, sec, A)
#     
# #     #サイン波をwavファイルとして書き出し
#     wave_Params = (1, 2, fs, len(binwave), 'NONE', 'not compressed')
# #     wave_Params = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
# 
#     '''###################
#         dirs        
#     ###################'''
#     dname_Audios = "data.46_1\\audios"
#     
#     if not os.path.isdir(dname_Audios) : os.makedirs(dname_Audios)
# 
# #     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
#     fname_Out = "%s\\output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
#                 (dname_Audios
#                 , libs.get_TimeLabel_Now()
#                 , fs, f0
#                 , "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #     fname_Out = "audios/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
# #                 (libs.get_TimeLabel_Now(), fs, f0, "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #                 (get_TimeLabel_Now(), fs, f0, "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%d_sec-%d.wav" % \
# #                 (get_TimeLabel_Now(), fs, f0, phase, sec)
#     
#     save_Wave(fname_Out, wave_Params, binwave)
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
