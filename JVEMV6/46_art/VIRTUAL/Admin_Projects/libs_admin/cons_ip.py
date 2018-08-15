'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\cons_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    at      : 2018/06/08 10:10:11
'''

#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class DfltVals(Enum):
    
    #get_4Corners__Corner_Width      = 200
    get_4Corners__Corner_Width      = 100
#     get_4Corners__Corner_Width      = 280
    #get_4Corners__Corner_Padding    = 20
    get_4Corners__Corner_Padding    = 10

    '''###################
        dos attack        
    ###################'''
    numOf_DosAttack = 0

class ColorThresholds(Enum):
    
    '''######################################
        Red
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isRed_Max_Val_R__Lower = 2.2 * 1000
#    isRed_Max_Val_R__Lower = 2.0 * 1000
#    isRed_Max_Val_R__Lower = 1.85 * 1000
    #isRed_Max_Val_R__Lower = 1.70 * 1000
    isRed_Max_Val_R__Lower = 1.60 * 1000
    isRed_Max_Val_R__Upper = 6.0 * 1000
#    isRed_Max_Val_R__Upper = 4.7 * 1000
#     isRed_Max_Val_R__Upper = 3.9 * 1000
    
    
    # G
#     isRed_Max_Val_G__Lower = 2.3 * 1000
#    isRed_Max_Val_G__Lower = 2.0 * 1000
#    isRed_Max_Val_G__Lower = 1.85 * 1000
    isRed_Max_Val_G__Lower = 1.70 * 1000
    isRed_Max_Val_G__Upper = 5.5 * 1000	#=> 20180709_060511
#    isRed_Max_Val_G__Upper = 4.7 * 1000
#     isRed_Max_Val_G__Upper = 3.9 * 1000
    
    # B
#    isRed_Max_Val_B__Lower = 1.6 * 1000
#    isRed_Max_Val_B__Lower = 1.35 * 1000
    isRed_Max_Val_B__Lower = 1.00 * 1000
#     isRed_Max_Val_B__Lower = 1.8 * 1000
#    isRed_Max_Val_B__Upper = 2.5 * 1000
    isRed_Max_Val_B__Upper = 4.25 * 1000
#    isRed_Max_Val_B__Upper = 3.5 * 1000
#     isRed_Max_Val_B__Upper = 3.1 * 1000
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
#    isRed_IdxOf_Max_R__Upper = 50
#     isRed_IdxOf_Max_R__Upper = 70
    isRed_IdxOf_Max_R__Upper = 91
    isRed_IdxOf_Max_R__Lower = 0
     
    # G
    #isRed_IdxOf_Max_G__Upper = 60
    #isRed_IdxOf_Max_G__Upper = 80
    isRed_IdxOf_Max_G__Upper = 105
    isRed_IdxOf_Max_G__Lower = 0
     
    # B
#     isRed_IdxOf_Max_B__Upper = 200
#    isRed_IdxOf_Max_B__Upper = 210
#    isRed_IdxOf_Max_B__Upper = 230
    isRed_IdxOf_Max_B__Upper = 250
    isRed_IdxOf_Max_B__Lower = 150
     

    '''######################################
        Green
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isGreen_Max_Val_R__Lower = 3.0 * 1000
#     isGreen_Max_Val_R__Lower = 2.6 * 1000
    isGreen_Max_Val_R__Lower = 1.8 * 1000
    isGreen_Max_Val_R__Upper = 5.4 * 1000
    #isGreen_Max_Val_R__Upper = 5.3 * 1000
#     isGreen_Max_Val_R__Upper = 4.1 * 1000
    
    # G
    isGreen_Max_Val_G__Lower = 1.4 * 1000
    isGreen_Max_Val_G__Upper = 4.95 * 1000
#    isGreen_Max_Val_G__Upper = 4.5 * 1000
#     isGreen_Max_Val_G__Upper = 3.7 * 1000
#     isGreen_Max_Val_G__Upper = 3.2 * 1000
#     isGreen_Max_Val_G__Upper = 2.8 * 1000
#     isGreen_Max_Val_G__Upper = 2.6 * 1000
    
    # B
    #isGreen_Max_Val_B__Lower = 2.0 * 1000
    isGreen_Max_Val_B__Lower = 1.85 * 1000
    isGreen_Max_Val_B__Upper = 4.85 * 1000
    #isGreen_Max_Val_B__Upper = 4.3 * 1000
#     isGreen_Max_Val_B__Upper = 3.2 * 1000
    
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
#     isGreen_IdxOf_Max_R__Upper = 50
#    isGreen_IdxOf_Max_R__Upper = 65
    #isGreen_IdxOf_Max_R__Upper = 120
    isGreen_IdxOf_Max_R__Upper = 130
    isGreen_IdxOf_Max_R__Lower = 0
     
    # G
#     isGreen_IdxOf_Max_G__Upper = 170
#     isGreen_IdxOf_Max_G__Upper = 210
#     isGreen_IdxOf_Max_G__Upper = 240
    isGreen_IdxOf_Max_G__Upper = 255
    isGreen_IdxOf_Max_G__Lower = 80
     
    # B
#     isGreen_IdxOf_Max_B__Upper = 200
#     isGreen_IdxOf_Max_B__Upper = 120
#     isGreen_IdxOf_Max_B__Upper = 145
    #isGreen_IdxOf_Max_B__Upper = 160
    isGreen_IdxOf_Max_B__Upper = 175
    isGreen_IdxOf_Max_B__Lower = 50
     

    '''######################################
        Yellow
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # max values
    # R
#     ts_Max_Val_R__Lower = 4000
#    isYellow_Max_Val_R__Lower = 2500
#     isYellow_Max_Val_R__Lower = 2.2 * 1000
    isYellow_Max_Val_R__Lower = 1.6 * 1000
    isYellow_Max_Val_R__Upper = 6.4 * 1000
#     isYellow_Max_Val_R__Upper = 5.8 * 1000
#     isYellow_Max_Val_R__Upper = 5000
    
    
    # G
#     isYellow_Max_Val_G__Lower = 3000
#    isYellow_Max_Val_G__Lower = 1.6 * 1000
    isYellow_Max_Val_G__Lower = 1.1 * 1000
    isYellow_Max_Val_G__Upper = 6.3 * 1000
#    isYellow_Max_Val_G__Upper = 4000
#     isYellow_Max_Val_G__Upper = 5.4 * 1000
#     isYellow_Max_Val_G__Upper = 4.8 * 1000
    
    # B
#     isYellow_Max_Val_B__Lower = 3500
#     isYellow_Max_Val_B__Lower = 2000
#    isYellow_Max_Val_B__Lower = 1.6 * 1000
#     isYellow_Max_Val_B__Lower = 1.4 * 1000
    isYellow_Max_Val_B__Lower = 1.2 * 1000
    isYellow_Max_Val_B__Upper = 10.8 * 1000 #=> 20180709_064100
#    isYellow_Max_Val_B__Upper = 6.2 * 1000
#     isYellow_Max_Val_B__Upper = 5.8 * 1000
#     isYellow_Max_Val_B__Upper = 4500
    
#     isYellow_Max_Val_G = 2000
#     isYellow_Max_Val_B = 2000

    '''###################
        thresholds : index of max values
    ###################'''    
    # index of max values
    # R
    isYellow_IdxOf_Max_R__Upper = -1      # -1 ==> not used
#    isYellow_IdxOf_Max_R__Lower = 80
    isYellow_IdxOf_Max_R__Lower = 115
#     isYellow_IdxOf_Max_R__Lower = 95
     
    # G

    isYellow_IdxOf_Max_G__Upper = 250
    isYellow_IdxOf_Max_G__Lower = 115
    #isYellow_IdxOf_Max_G__Lower = 130
#     isYellow_IdxOf_Max_G__Upper = 220
#     isYellow_IdxOf_Max_G__Lower = 145
#     isYellow_IdxOf_Max_G__Lower = 165
#     isYellow_IdxOf_Max_G__Lower = 180
     
    # B
#     isYellow_IdxOf_Max_B__Upper = 200
#     isYellow_IdxOf_Max_B__Upper = 180
#     isYellow_IdxOf_Max_B__Upper = 165
#     isYellow_IdxOf_Max_B__Upper = 240
    isYellow_IdxOf_Max_B__Upper = 255
    isYellow_IdxOf_Max_B__Lower = 140      # -1 ==> not used

    '''######################################
        White
    ######################################'''
    '''###################
        thresholds : index of max values
    ###################'''    
    isWhite_IdxOf_Max = 245
#     isWhite_IdxOf_Max = 255
    
    '''###################
        thresholds : max values
    ###################'''
    # R
    isWhite_Max_Val__Lower = 14 * 1000
#     isWhite_Max_Val__Lower = 26 * 1000
#     isYellow_Max_Val_R__Upper = 5000

    '''######################################
        Black
    ######################################'''
    '''###################
        thresholds : index of max values
    ###################'''    
    isBlack_IdxOf_Max = 0
    
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isBlack_Max_Val__Lower = 21 * 1000
    #isBlack_Max_Val__Lower = 16 * 1000
    isBlack_Max_Val__Lower = 15 * 1000
#     isBlack_Max_Val__Lower = 26 * 1000


    '''######################################
        thresholds : HSV
    ######################################'''
    '''###################
        yellow        
    ###################'''
    #isYellow_HSV_Variance__Upper = 0.3
    isYellow_HSV_Variance__Upper = 0.65
    isYellow_HSV_Variance__Lower = 0.0
    #isYellow_HSV_Variance__Lower = 0.002
#     isYellow_HSV_Variance__Lower = 0.01
    
#     isYellow_HSV_Average__Upper = 90.0
    #isYellow_HSV_Average__Upper = 93.0
    #isYellow_HSV_Average__Upper = 97.0
    isYellow_HSV_Average__Upper = 98.0
    isYellow_HSV_Average__Lower = 88.0
    
    '''###################
        red        
    ###################'''
#     isRed_HSV_Variance__Upper = 0.3
    #isRed_HSV_Variance__Upper = 0.40
    isRed_HSV_Variance__Upper = 0.43
    isRed_HSV_Variance__Lower = 0.002
#     isRed_HSV_Variance__Lower = 0.01
    
    isRed_HSV_Average__Upper = 124.0
    isRed_HSV_Average__Lower = 116.0
#     isRed_HSV_Average__Lower = 120.0
    
    '''###################
        green        
    ###################'''
#     isGreen_HSV_Variance__Upper = 0.3
    #isGreen_HSV_Variance__Upper = 0.38
    isGreen_HSV_Variance__Upper = 0.60
    isGreen_HSV_Variance__Lower = 0.002
#     isGreen_HSV_Variance__Lower = 0.01
    
#     isGreen_HSV_Average__Upper = 72.0
#     isGreen_HSV_Average__Upper = 75.0
    #isGreen_HSV_Average__Upper = 79.0
    isGreen_HSV_Average__Upper = 83.0
    isGreen_HSV_Average__Lower = 67.0
#     isGreen_HSV_Average__Lower = 70.0
    
    '''###################
        black        
    ###################'''
    isBlack_HSV_Variance__Upper = 0.00
    isBlack_HSV_Variance__Lower = 0.00
    
    isBlack_HSV_Average__Upper = 0.0
    isBlack_HSV_Average__Lower = 0.0
    
#/ class ColorThresholds(Enum):    

class FilePaths(Enum):
    
    dpath_LogFile = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
    
    fname_LogFile = "get_4_corners.log"
    
    fname_LogFile__Gradation = "gradation.log"
    
#/ class ColorThresholds(Enum):
    
class ColorNameSet(Enum):

    lo_Color_Sets = [
        
            "oooo"
            
#             '''###################
#                 r,g,y ==> each only        # 3 types
#             ###################'''
            , "ooor"    # UNDEFINED
            , "gooo"    # ":m 食べた物　間食 / 砂糖菓子"
            , "oooy"    # :m 食べた物
            , "oowy"    # :m 食べた物
            
#             '''###################
#                 r,g,y ==> each, 2        # 3 types
#             ###################'''
            , "oorr"
            , "ggoo"    # :m 食べた物　間食 / ヨーグルト / +=
            , "ooyy"    # delete

#             '''###################
#                 r,g,y ==> each, 3        # 3 types
#             ###################'''
            , "owww"    # 読みたい本
            
#             '''###################
#                 r,g,y ==> each, 4        # 3 types
#             ###################'''
            , "aaaa"    # 読みたい本
            , "wwww"    # 読みたい本
    
#             '''###################
#                 r,g,y ==> 1 each, 2 kinds        # 3 types
#             ###################'''
            , "goor"    # :m XXX
            , "gooy"
            , "oory"    # 読んだ本
            
#             '''###################
#                 r,g,y ==> 1 or 2 each, 2 kinds        # 3 types
#             ###################'''
            # 1 a / 2 w / 
            , "aoww"    # 読みたい本
            
            # 2 a / 2 1 / 
            , "aaow"    # 読みたい本
            
            
        ]
#     lo_Color_Sets = [
#         
#             "oooo"
#             
#             '''###################
#                 r,g,y ==> each only        # 3 types
#             ###################'''
#             , "ooor"    # UNDEFINED
#             , "gooo"    # ":m 食べた物　間食 / 砂糖菓子"
#             , "oooy"    # :m 食べた物
#             
#             '''###################
#                 r,g,y ==> each, 2        # 3 types
#             ###################'''
#             , "oorr"
#             , "ggoo"    # :m 食べた物　間食 / ヨーグルト / +=
#             , "ooyy"    # delete
#     
#             '''###################
#                 r,g,y ==> 1 each, 2 kinds        # 3 types
#             ###################'''
#             , "goor"
#             , "gooy"
#             , "oory"    # 読んだ本
#     
#         ]
    
    do_Color_Sets_Memo = {
        
            "oooo" : ""

#             '''###################
#                 r,g,y ==> each only        # 3 types
#             ###################'''
#            , "ooor" : "UNDEFINED"
            , "ooor" : u':m music / log / XXX / '
            , "gooo" : ":m 食べた物　間食 / 砂糖菓子or乾物菓子"
            , "oooy" : u':m 食べた物'
            , "oowy" : u':m 食べた物'
            
            
#             '''###################
#                 r,g,y ==> each, 2        # 3 types
#             ###################'''
#             , "oorr"
            , "ggoo" : u':m 食べた物　間食 / ヨーグルト / += '
            , "ooyy" : u'\'-*'
            , "oorr" : u'MEMO'
            #, "oorr" : uMEMO'UNDEFINED'

#             '''###################
#                 r,g,y ==> each, 3        # 3 types
#             ###################'''
            , "owww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            
#             '''###################
#                 r,g,y ==> each, 4        # 3 types
#             ###################'''
            , "aaaa" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            , "wwww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本

#             '''###################
#                 r,g,y ==> 1 each, 2 kinds        # 3 types
#             ###################'''
            #, "goor" : u'UNDEFINED'
            , "goor" : u':m XXX'
            
            , "gooy" : u'\'-*'
            , "oory" : u':bookmemo / 読んだ本 / 『』 / 著者=XXX'

#             '''###################
#                 r,g,y ==> 1 or 2 each, 2 kinds        # 3 types
#             ###################'''
            , "aoww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            , "aaow" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本


        }

    memo_Unknown = "UNKNOWN"
    
    colName_Red = "red"
    colName_Yellow = "yellow"
    colName_Green = "green"
    colName_White = "white"
    colName_Black = "black"
    
#/ class ColorNameSet(Enum):
    