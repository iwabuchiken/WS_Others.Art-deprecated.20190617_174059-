'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\cons_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    at      : 2018/06/08 10:10:11
'''

#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class DfltVals(Enum):
    
    get_4Corners__Corner_Width      = 200
#     get_4Corners__Corner_Width      = 280
    get_4Corners__Corner_Padding    = 20

class ColorThresholds(Enum):
    
    '''######################################
        Red
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
    isRed_Max_Val_R__Lower = 2.2 * 1000
    isRed_Max_Val_R__Upper = 3.9 * 1000
    
    # G
    isRed_Max_Val_G__Lower = 2.3 * 1000
    isRed_Max_Val_G__Upper = 3.9 * 1000
    
    # B
    isRed_Max_Val_B__Lower = 1.8 * 1000
    isRed_Max_Val_B__Upper = 2.5 * 1000
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
    isRed_IdxOf_Max_R__Upper = 50
    isRed_IdxOf_Max_R__Lower = 0
     
    # G
    isRed_IdxOf_Max_G__Upper = 60
    isRed_IdxOf_Max_G__Lower = 0
     
    # B
    isRed_IdxOf_Max_B__Upper = 200
    isRed_IdxOf_Max_B__Lower = 150
     

    '''######################################
        Yellow
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # max values
    # R
#     ts_Max_Val_R__Lower = 4000
    isYellow_Max_Val_R__Lower = 2500
    isYellow_Max_Val_R__Upper = 5000
    
    # G
#     isYellow_Max_Val_G__Lower = 3000
    isYellow_Max_Val_G__Lower = 2000
    isYellow_Max_Val_G__Upper = 4000
    
    # B
#     isYellow_Max_Val_B__Lower = 3500
    isYellow_Max_Val_B__Lower = 2000
    isYellow_Max_Val_B__Upper = 4500
    
#     isYellow_Max_Val_G = 2000
#     isYellow_Max_Val_B = 2000

    '''###################
        thresholds : index of max values
    ###################'''    
    # index of max values
    # R
    isYellow_IdxOf_Max_R__Upper = -1      # -1 ==> not used
    isYellow_IdxOf_Max_R__Lower = 80
     
    # G
    isYellow_IdxOf_Max_G__Upper = 220
    isYellow_IdxOf_Max_G__Lower = 145
#     isYellow_IdxOf_Max_G__Lower = 165
#     isYellow_IdxOf_Max_G__Lower = 180
     
    # B
#     isYellow_IdxOf_Max_B__Upper = 200
#     isYellow_IdxOf_Max_B__Upper = 180
    isYellow_IdxOf_Max_B__Upper = 165
    isYellow_IdxOf_Max_B__Lower = -1      # -1 ==> not used

