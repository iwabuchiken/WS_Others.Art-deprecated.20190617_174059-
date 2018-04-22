# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\JVEMV6\34\_2
test_JVEMV6_34_2.py


'''
###############################################
import sys
# from sympy.solvers.tests.test_constantsimp import C2
sys.path.append('.')
sys.path.append('..')
from libs import libs        #=> C:\WORKS_2\WS\Eclipse_Luna\C_SoundProg\python\libs
# from libs.libs import *        #=> C:\WORKS_2\WS\Eclipse_Luna\C_SoundProg\python\libs
# import libs.libs as lib
# from libs.libs import *        #=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
                            #=> ref : http://qiita.com/Usek/items/86edfa0835292c80fff5
# from libs import *        #=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
                        #=> libs.py : C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\libs.py

import libs.labs as labs

import getopt
import os
import inspect

import math as math

import matplotlib as mt
import numpy as np



############################
#    Funcs
############################
def show_Message() :
                
    msg = '''
    yes'''
    
    print (msg)
#     print msg

if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''
    args = sys.argv
    
    if '-h' in args or '-help' in args : 
        show_Message()
        
        sys.exit(1)

    '''###################
        get options        
    ###################'''
    keychars = "vf"
    
    result = libs.get_opt_2(sys.argv, keychars)

    '''###################
        evecute        
    ###################'''
     
    print
    print("[%s:%d] done" % (libs.thisfile(), libs.linenum()))
