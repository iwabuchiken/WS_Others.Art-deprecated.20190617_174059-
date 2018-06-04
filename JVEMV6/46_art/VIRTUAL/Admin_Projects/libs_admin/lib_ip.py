'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
    at      : 2018/05/26 13:29:43
'''
'''###################
    import : built-in modules        
###################'''
import inspect, os, sys, cv2

from enum import Enum
#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time

'''###################
    import : use-installed modules        
###################'''
from sympy.physics.vector.printing import params
import numpy as np

from scipy.stats import skew

'''###################
    import : orig modules        
###################'''
# sys.path.append('.')

#C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
from libs_admin import libs #=> working
# import libs

'''#########################################################
    enums        
#########################################################'''

'''#########################################################
    functions        
#########################################################'''
'''###################
    get_Std_Dev(lo_Data)
    
    at : 
    
    @return: dictionary of skew values        
    
        {'R' : 1.1002928031008152, 
            'G' : 4.955577672343114,
            'B' : 6.775475308994965 }
    
###################'''
def get_Std_Dev(lo_Data):
    
    '''###################
        get : mean value        
    ###################'''
    # values of each color composite
#     valsOf_R = [x * 0.001 for x in lo_Data]
#     valsOf_R = [x * np.power(10, -3) for x in lo_Data]
    valsOf_R = lo_Data
#     valsOf_R = do_Image_MetaData['valsOf_R']
    
#     #debug
#     print()
#     print("[%s:%d] valsOf_R[0:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(valsOf_R[0:10])
    
    # sum
    sumOf_ValsOf_R = sum(valsOf_R)

    # mean
    meanOf_R = sumOf_ValsOf_R / len(valsOf_R)
    
#     #debug
#     print()
#     print("[%s:%d] meanOf_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , meanOf_R
#         ), file=sys.stderr)
    
    # vals squared
    valsSquared_R = [np.power(x, 2) for x in valsOf_R]
    
#     #debug
#     print()
#     print("[%s:%d] valsSquared_R[0:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(valsSquared_R[0:10])


    # summation of vals squared
    summationOf_ValsSquared_R = sum(valsSquared_R)
#     summationOf_ValsSquared_R = sum[valsSquared_R]

#     #debug
#     print()
#     print("[%s:%d] summationOf_ValsSquared_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , summationOf_ValsSquared_R
#         ), file=sys.stderr)
    
    # length
    lenOf_R = len(valsOf_R)
    
    # standard dev
    variance_R = 1.0 * summationOf_ValsSquared_R / lenOf_R - np.power(meanOf_R, 2)
    
#     #debug
#     print()
#     print("[%s:%d] variance_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , variance_R
#         ), file=sys.stderr)
    
    # standard dev
    stdDev_R = np.sqrt(variance_R)

    '''###################
        return        
    ###################'''
    return stdDev_R
    
#/ def get_Std_Dev(lo__Data):
    
'''###################
    get_Moment(valsOf_ColorComposite, moment_Num)
    
    @return: Nnd moment        
                e.g. 4.955577672343114,
    
###################'''
def get_Moment(valsOf_ColorComposite, moment_Num):
    
    # length
    lenOf_Vals = len(valsOf_ColorComposite)
    
#     # stddev
#     stddev = get_Std_Dev(valsOf_ColorComposite)
    
    # average
    avg = sum(valsOf_ColorComposite) / lenOf_Vals
    
    lo_Power = [np.power(x - avg, moment_Num) for x in valsOf_ColorComposite]
    
    moment = sum(lo_Power) / lenOf_Vals
#     moment = sum(lo_Power) / lenOf_Vals / np.power(stddev, moment_Num)
    
    '''###################
        return        
    ###################'''
    return moment

#/ def get_Moment(valsOf_ColorComposite, 3):

'''###################
    get_Skew_Value(valsOf_ColorComposite)
    
    @return: skew value (float)        
                e.g. 4.955577672343114,
    
###################'''
# def get_Skew_Value(lo_Image_Data):
def get_Skew_Value(valsOf_ColorComposite):
    
    '''###################
        prep        
    ###################'''

    '''###################
        get : std dev
    ###################'''
    # values of each color composite
#     valsOf_R = valsOf_ColorComposite
    
    # std dev
    stdDev = get_Std_Dev(valsOf_ColorComposite)
#     stdDev_R = get_Std_Dev(valsOf_R)
    
#     #debug
#     print()
#     print("[%s:%d] stdDev_R = %.05f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , stdDev_R
#             ), file=sys.stderr)
    
    '''###################
        get : moment : 3
    ###################'''
    moment_Number = 3
    
    moment_3 = get_Moment(valsOf_ColorComposite, moment_Number)
    
    '''###################
        skew
    ###################'''
    skew = 1.0 * moment_3 / stdDev
    
    '''###################
        return        
    ###################'''
    return skew
#     return -999
    
#     pass
    
#/ def get_Skew_Value(list):

'''###################
    get_Skews(img_Data)
    
    @return: dictionary of skew values        
    
        {'R' : 1.1002928031008152, 
            'G' : 4.955577672343114,
            'B' : 6.775475308994965 }
    
###################'''
def get_Skews(img_Data):
    
    '''###################
        vars
    ###################'''
    do_Skews = {"skew_R" : -1, "skew_G" : -1, "skew_B" : -1}
    
    '''###################
        skew : prep
    ###################'''
    # meta data
    do_Image_MetaData = get_Image_MetaData_Basic(img_Data)
    
    # tuple of vals
    valsOf_R = do_Image_MetaData['valsOf_R']
    valsOf_G = do_Image_MetaData['valsOf_G']
    valsOf_B = do_Image_MetaData['valsOf_B']
    
#     to_Vals = (valsOf_R, valsOf_G, valsOf_B)
    
    '''###################
        skew
        
        ref : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\2_\2_1.py
    ###################'''
    # adjust values
    valOf_Adjust = 0.01
    
    valsOf_R__ = [x * valOf_Adjust for x in valsOf_R]
    valsOf_G__ = [x * valOf_Adjust for x in valsOf_G]
    valsOf_B__ = [x * valOf_Adjust for x in valsOf_B]
    
    do_Skews['skew_R'] = get_Skew_Value(valsOf_R__)
    do_Skews['skew_G'] = get_Skew_Value(valsOf_G__)
    do_Skews['skew_B'] = get_Skew_Value(valsOf_B__)
#     do_Skews['skew_R'] = get_Skew_Value(valsOf_R)
#     do_Skews['skew_G'] = get_Skew_Value(valsOf_G)
#     do_Skews['skew_B'] = get_Skew_Value(valsOf_B)
#     do_Skews['skew_R'] = skew(valsOf_R)
#     do_Skews['skew_G'] = skew(valsOf_G)
#     do_Skews['skew_B'] = skew(valsOf_B)
    
#     # sum
#     sumOf_ValsOf_R = sum(valsOf_R)
#     sumOf_ValsOf_G = sum(valsOf_G)
#     sumOf_ValsOf_B = sum(valsOf_B)
#     
# #     print()
# #     print("[%s:%d] sumOf_ValsOf_R = %d, sumOf_ValsOf_G = %d, sumOf_ValsOf_B = %d" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , sumOf_ValsOf_R, sumOf_ValsOf_G, sumOf_ValsOf_B
# #             ), file=sys.stderr)
# #     print("[%s:%d] sumOf_ValsOf_R => %d" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , sumOf_ValsOf_R
# #             ), file=sys.stderr)
# 
#     # means
#     meanOf_R = sumOf_ValsOf_R / len(valsOf_R)
#     meanOf_G = sumOf_ValsOf_G / len(valsOf_G)
#     meanOf_B = sumOf_ValsOf_B / len(valsOf_B)
#     
# #     #debug
# #     print()
# #     print("[%s:%d] meanOf_R = %.03f, meanOf_G = %.03f, meanOf_B = %.03f" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , meanOf_R, meanOf_G, meanOf_B
# #             ), file=sys.stderr)
#     
#     # summation
#     lo_PowerOf_R_3 = [np.power((x - meanOf_R), 3) for x in valsOf_R]
# #     lo_PowerOf_3_R = [x * 3 for x in valsOf_R]
# #     summationOf_R = [x * 3 for x in valsOf_R]
# #     summationOf_R = sum[np.power((x - meanOf_R), 3) for x in valsOf_R]
#     
#     summationOf_R_3 = sum[lo_PowerOf_R_3]
#     
#     # squares of Rs
#     
    
    '''###################
        return        
    ###################'''
    return do_Skews
#     return -1
    
#/ def get_Skew(img_Data):

'''###################
    get_Image_MetaData_Basic(img_Data)
    
    at : 2018/05/28 07:59:22
    
    @return:     
        do_MetaData['max_R'] = max_R
        do_MetaData['max_G'] = max_G
        do_MetaData['max_B'] = max_B
        
        do_MetaData['min_R'] = min_R
        do_MetaData['min_G'] = min_G
        do_MetaData['min_B'] = min_B
        
        do_MetaData['valsOf_R'] = valsOf_R
        do_MetaData['valsOf_G'] = valsOf_G
        do_MetaData['valsOf_B'] = valsOf_B        
###################'''
def get_Image_MetaData_Basic(img_Data):
    
    '''###################
        vars        
    ###################'''
    do_MetaData = {}
    
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

    for row in img_Data:
#     for row in item:
    
        for cell in row:
            
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
    
    # set : data
    
    do_MetaData['max_R'] = max_R
    do_MetaData['max_G'] = max_G
    do_MetaData['max_B'] = max_B
    
    do_MetaData['min_R'] = min_R
    do_MetaData['min_G'] = min_G
    do_MetaData['min_B'] = min_B
    
    do_MetaData['valsOf_R'] = valsOf_R
    do_MetaData['valsOf_G'] = valsOf_G
    do_MetaData['valsOf_B'] = valsOf_B
    
#     lo_Image_MetaData.append(
#         [
# #                 valsOf_R
# #                 , valsOf_G
# #                 , valsOf_B
#             
# #                 , max_R
#             max_R
#             , max_G
#             , max_B
#             
#             , min_R
#             , min_G
#             , min_B
#             
#             , valsOf_R
#             , valsOf_G
#             , valsOf_B
#             ]
#     )
        
    '''###################
        return        
    ###################'''
    return do_MetaData
    
#/ def get_Image_MetaData_Basic(img_Data):

'''###################
    get_IdxOf_Maxes(img_Data)
    
    @param img_Data: [
                        [ 
                            [103 101  93], [100  98  90],..., [ 72  80  10] 
                        ],
                        [ 
                            [103 101  93], [100  98  90],..., [ 72  80  10] 
                        ],
                        ...
                    ]
    
###################'''
def get_IdxOf_Maxes(img_Data):

    '''###################
        metadata        
    ###################'''
    # meta data
    do_Image_MetaData = get_Image_MetaData_Basic(img_Data)
    
    # tuple of vals
    valsOf_R = do_Image_MetaData['valsOf_R']
    valsOf_G = do_Image_MetaData['valsOf_G']
    valsOf_B = do_Image_MetaData['valsOf_B']

    
    '''###################
        vars        
    ###################'''
    # index
    idxOf_Max_R = -1
    idxOf_Max_G = -1
    idxOf_Max_B = -1

    # vals
    maxVal_R = -1
    maxVal_G = -1
    maxVal_B = -1
    
    # counter
    cntOf_R = 0
    cntOf_G = 0
    cntOf_B = 0
    
    '''###################
        iteration        
    ###################'''
    '''###################
        red
    ###################'''
    for val in valsOf_R:
        
        # judge
        if val > maxVal_R : 
            maxVal_R = val; idxOf_Max_R = cntOf_R
        
        # count
        cntOf_R += 1
        
    #/for val in valsOf_R:
    
    '''###################
        G
    ###################'''
    for val in valsOf_G:
        
        # judge
        if val > maxVal_G : 
            maxVal_G = val; idxOf_Max_G = cntOf_G
        
        # count
        cntOf_G += 1
        
    #/for val in valsOf_G:
    
    '''###################
        B
    ###################'''
    for val in valsOf_B:
        
        # judge
        if val > maxVal_B : 
            maxVal_B = val; idxOf_Max_B = cntOf_B
        
        # count
        cntOf_B += 1
        
    #/for val in valsOf_B:
    
#     print()
#     print("[%s:%d] idxOf_Max_R = %d, len(valsOf_R) = %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , idxOf_Max_R, len(valsOf_R)
#             ), file=sys.stderr)
#     
    
#     iteration
#     for xs in img_Data:
#         
#         for ys in xs:
#         
# #             #debug
# #             print()
# #             print("[%s:%d] vals =>" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #             print(vals)
# 
#             # get : elem vals
#             R = ys[0]
#             G = ys[1]
#             B = ys[2]
#             
#             # update max val, idx of max
#             if R > maxVal_R : 
#                 maxVal_R = R
#                 idxOf_Max_R = cntOf_R
#                 
#             if G > maxVal_G : maxVal_G = G; idxOf_Max_G = cntOf_G
#             if B > maxVal_B : maxVal_B = B; idxOf_Max_B = cntOf_B
#             
#             # counter
#             cnt
# 
#         
#     #/for vals in img_Data:
    
    '''###################
        return        
    ###################'''
    return idxOf_Max_R, idxOf_Max_G, idxOf_Max_B, \
            maxVal_R, maxVal_G, maxVal_B

#/ def get_IdxOf_Maxes(img_Data):

def is_CornerOf_Green__PhotoOf_Sweets(image_StatsData):
    
    '''###################
        vars        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
    print()
    print("[%s:%d] idxOf_Maxes =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

    print()
    print("[%s:%d] max_Vals =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(max_Vals)
    
    '''###################
        judge        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    # thresholds
    ts_Max_Val_R = 5500
    ts_Max_Val_G = 5500
    ts_Max_Val_B = 500

    # judge : index of max val
    # 'B' ===> color element of R (data is obtained in BGR format)
    if idxOf_Maxes_B > 20 : 
        
        msg = "False : idxOf_Maxes_B > 20 (%d)" % idxOf_Maxes_B
        
        print()
#         print("[%s:%d] False : idxOf_Maxes_B > 20 (%d)" % \
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            ), file=sys.stderr)
        
        return False, msg
    
    if idxOf_Maxes_G < 30 or idxOf_Maxes_G > 80 : 

#         print()
#         print("[%s:%d] False : idxOf_Maxes_G < 30 or idxOf_Maxes_G > 80" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False
        
        msg = "False : idxOf_Maxes_G < 30 or idxOf_Maxes_G > 80 (%d)" % idxOf_Maxes_G
        
        print()
#         print("[%s:%d] False : idxOf_Maxes_B > 20 (%d)" % \
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            ), file=sys.stderr)
        
        return False, msg

    if idxOf_Maxes_R < 30 or idxOf_Maxes_R > 80 : 
        
#         print()
#         print("[%s:%d] False : idxOf_Maxes_R < 30 or idxOf_Maxes_R > 80" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : idxOf_Maxes_R < 30 or idxOf_Maxes_R > 80 (%d)" % idxOf_Maxes_R
        
        print()
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            ), file=sys.stderr)
        
        return False, msg

    # judge : max vals
#     if max_Val_R < 5000 : 
#     if max_Val_R > 5000 : 
    if max_Val_R > ts_Max_Val_R : 
        
        
        
#         print()
# #         print("[%s:%d] False : max_Val_R < 5000" % \
#         print("[%s:%d] False : max_Val_R > 5000 (%d)" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , max_Val_R
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : max_Val_R > 5000 (%d)" % max_Val_R
        
        print()
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            ), file=sys.stderr)
        
        return False, msg

#     if max_Val_G < 5000 : 
#     if max_Val_G > 5000 : 
    if max_Val_G > ts_Max_Val_G : 

#         print()
#         print("[%s:%d] False : max_Val_G > 5000" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : max_Val_G > 5000 (%d)" % max_Val_G
        
        print()
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            ), file=sys.stderr)
        
        return False, msg


    if max_Val_B < 5000 or max_Val_B > 7500 : 

#         print()
#         print("[%s:%d] False : max_Val_B < 5000 or max_Val_B > 7500" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False
        
        '''###################
            judge : index of max val ==> 0?        
        ###################'''
        if max_Val_B > 7500 and not idxOf_Maxes_B == 0 : #if max_Val_B > 7500 and not idxOf_Maxes_B == 0
        
            msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d, idxOf_Max = %d)" \
                    % (max_Val_B, idxOf_Maxes_B)
            
            print()
            print("[%s:%d] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , msg
                ), file=sys.stderr)
            
            return False, msg
            
        #/if max_Val_B > 7500 and not idxOf_Maxes_B == 0
        
        
#         msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d)" % max_Val_B
#         msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d, idxOf_Max = %d)" \
#                 % (max_Val_B, idxOf_Maxes_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
#         
#         return False, msg

    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_CornerOf_Green(image_StatsData):
'''###################
    get_Corner_Images(img_Src, corner_Length)        
    
    @return: [left bottom, right bottom, left up, right up]

    |------------------------|
    |(2)                  (3)|
    |                        |
    |                        |
    |                        |
    |(0)                  (1)|
    |------------------------|
    
###################'''
# def get_Corner_Images(img_Src, corner_Length) :
def get_Corner_Images(img_Src, corner_Length, padding = 0) :
    
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

# def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images, lo_Image_MetaData):

def is_PhotoOf__Sweets(dpath_Images, fname_Image) :
    
    '''###################
                
    ###################'''
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
        msg = "file NOT exist : %s" % fpath_Image
        
        # return
        return False, msg
    
        # cv instance
    img_Orig = cv2.imread(fpath_Image)
    
    print()
    print("[%s:%d] cv2 image ==> loaded" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    # convert to RGB
    img_RGB = img_Orig


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
    
    padding = 0
    
    img_Corners = get_Corner_Images(img_RGB, corner_Length, padding)
    
    print()
    print("[%s:%d] len(img_Corners) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(img_Corners)
        ), file=sys.stderr)

    '''###################
        save : images of 4 corners        
    ###################'''
    save_Image = False
    
    lo_Names_Of_Corner_Images = \
            get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image)
#             saveImage_4Corners(img_Corners, fname_Image, save_Image)
#             _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image)
    
    print()
    print("[%s:%d] lo_Names_Of_Corner_Images =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_Names_Of_Corner_Images)

    '''###################
        get : basic data
    ###################'''
    lo_Image_MetaData = get_4_corners__Get_MetaData(img_Corners)
#     lo_Image_MetaData = _exec_get_4_corners__Get_MetaData(img_Corners)

    '''###################
        get : stat data
    ###################'''
    lo_Image_StatsData = get_4_corners__Get_StatsData(img_Corners)
#     lo_Image_StatsData = _exec_get_4_corners__Get_StatsData(img_Corners)


    '''###################
        filtering : a corner of green ?
    ###################'''
    # lo_Image_StatsData[0] => left bottom corner
#         res = lib_ip.is_CornerOf_Green(lo_Image_StatsData[0])
#     res, comment = lib_ip.is_CornerOf_Green__PhotoOf_Sweets(lo_Image_StatsData[0])
    res, comment = is_CornerOf_Green__PhotoOf_Sweets(lo_Image_StatsData[0])

    print()
    print("[%s:%d] is_CornerOf_Green => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res
        ), file=sys.stderr)

    '''###################
        write log : file names
    ###################'''
#     _exec_get_4_corners__Write_Log(
    get_4_corners__Write_Log(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    , comment
                    )

    '''###################
        return        
    ###################'''
#     msg = "done"
    
    return res, comment, (height, width, channels)
#     return res, comment
#     return False, msg
    
#/ def is_PhotoOf__Sweets(dir_path, file_name) :

def get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image = True) :
    
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

        # cv2 : save image
        #ref https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/
        if save_Image == True : cv2.imwrite(fpath_Plot, item)
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

    
#/ def saveImage_4Corners(img_Corners, fname_Image) :

def get_4_corners__Get_MetaData(img_Corners) :
    
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

#/ def get_4_corners__Get_MetaData(img_Corners) :

def get_4_corners__Get_StatsData(img_Corners) :
    
    # data
    lo_Image_StatsData = []
    
    for img_Data in img_Corners:
        
        # var
        do_StasData = {}
        
        '''###################
            skews        
        ###################'''
        
        print("[%s:%d] getting skew values..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        skew_Values = get_Skews(img_Data)
#         skew = lib_ip.get_Skew(img_Data)
        
        do_StasData['skew_values'] = skew_Values
#         do_StasData['skew'] = skew
        
        # append
        lo_Image_StatsData.append(do_StasData)
        
        '''###################
            index of max        
        ###################'''
#         idxOf_Max_R, idxOf_Max_G, idxOf_Max_B = lib_ip.get_IdxOf_Maxes(img_Data)
        idxOf_Max_R, idxOf_Max_G, idxOf_Max_B, maxVal_R, maxVal_G, maxVal_B \
                    = get_IdxOf_Maxes(img_Data)
        
        print()
        print("[%s:%d] idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , idxOf_Max_R, idxOf_Max_G, idxOf_Max_B
        ), file=sys.stderr)
        
        do_StasData['idxOf_Maxes'] = [idxOf_Max_R, idxOf_Max_G, idxOf_Max_B]
        
        do_StasData['max_Vals'] = [maxVal_R, maxVal_G, maxVal_B]
        
    #/for img in img_Corners:

    '''###################
        return        
    ###################'''
    return lo_Image_StatsData
    
#/ def get_4_corners__Get_StatsData(img_Corners) :

def get_4_corners__Write_Log(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    , comment
                    ) :
    
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
    
    '''###################
        write : meta info        
    ###################'''
    msg = "dpath_Images = %s" % (dpath_Images)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    
    msg = "fname_Image = %s" % (fname_Image)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    fout_Log.write('\n')
    
    
    # iterate
    idxOf_Images = 0
    
    lenOf_LO_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for item in lo_Names_Of_Corner_Images:
    for i in range(lenOf_LO_Names_Of_Corner_Images):
    
        # items
        name = lo_Names_Of_Corner_Images[i]
        
        # meta data
        metaData = lo_Image_MetaData[i]
        
        # stats
                #         [{'skew_values': {'skew_B': 533.0519884872008, 'skew_R': 236.23069368923885, 'sk
                # ew_G': 238.3791814689376}}, {'skew_values': {'skew_B': 56.682440339675104, 'skew
                # _R': 149.4848026940312, 'skew_G': 78.97239727258551}}, {'skew_values': {'skew_B'
                # : 494.3158542205711, 'skew_R': 312.1150017522547, 'skew_G': 465.10712589168577}}
                # , {'skew_values': {'skew_B': 481.71441048360913, 'skew_R': 323.66383568902853, '
                # skew_G': 475.05481070433}}]
        do_Stats = lo_Image_StatsData[i]
        
        do_Skews = do_Stats['skew_values']
#         print()
#         print("[%s:%d] lo_Image_StatsData =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(lo_Image_StatsData)
#         
#         print()
#         print("[%s:%d] do_Stats =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(do_Stats)
        
        skew_R = do_Skews['skew_R']
        skew_G = do_Skews['skew_G']
        skew_B = do_Skews['skew_B']
#         skew_R = do_Stats['skew_R']
#         skew_G = do_Stats['skew_G']
#         skew_B = do_Stats['skew_B']
        
        '''###################
            file name
        ###################'''
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
        
        '''###################
            skews        
        ###################'''
        msg = "skew_R = %.04f, skew_G = %.04f, skew_B = %.04f" % \
                (
                    skew_R, skew_G, skew_B
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        '''###################
            index of max values,
            max values
        ###################'''
        idxOf_MaxVals = do_Stats['idxOf_Maxes']
        
        max_Vals = do_Stats['max_Vals']

#         msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
        msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
                (
                    idxOf_MaxVals[0], idxOf_MaxVals[1], idxOf_MaxVals[2]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        msg = "max_Vals_R = %d, max_Vals_G = %d, max_Vals_B = %d" % \
                (
                    max_Vals[0], max_Vals[1], max_Vals[2]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        '''###################
            raw data : histogram        
        ###################'''
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
#     fout_Log.write('\n')
    
    '''###################
        write : judge        
    ###################'''
#     fout_Log.write('\n')
    
#     msg = "dpath_Images = %s" % (dpath_Images)
#     
#     fout_Log.write(msg)
#     fout_Log.write('\n')
#     
#     msg = "fname_Image = %s" % (fname_Image)
#     
#     fout_Log.write(msg)
#     fout_Log.write('\n')
    
    
    msg = "is_CornerOf_Green__PhotoOf_Sweets => %s (%s)" % (res, comment)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    
    # close file
    fout_Log.close()
#/ get_4_corners__Write_Log
