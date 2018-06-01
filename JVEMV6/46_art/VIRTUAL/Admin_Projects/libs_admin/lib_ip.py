'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
    at      : 2018/05/26 13:29:43
'''
'''###################
    import : built-in modules        
###################'''
import inspect, os, sys
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