# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\JVEMV6\34\_3
34_3.py


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

#ref http://deeplearning.net/tutorial/gettingstarted.html
import _pickle as cPickle, gzip, numpy
# import cPickle, gzip, numpy


############################
#    Funcs
############################
def show_Message() :
                
    msg = '''
    yes'''
    
    print (msg)
#     print msg

def shared_dataset(data_xy):
    """ Function that loads the dataset into shared variables

    The reason we store our dataset in shared variables is to allow
    Theano to copy it into the GPU memory (when code is run on GPU).
    Since copying data into the GPU is slow, copying a minibatch everytime
    is needed (the default behaviour if the data is not in a shared
    variable) would lead to a large decrease in performance.
    """
    data_x, data_y = data_xy
    shared_x = theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX))
    shared_y = theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX))
    # When storing data on the GPU it has to be stored as floats
    # therefore we will store the labels as ``floatX`` as well
    # (``shared_y`` does exactly that). But during our computations
    # we need them as ints (we use labels as index, and if they are
    # floats it doesn't make sense) therefore instead of returning
    # ``shared_y`` we will have to cast it to int. This little hack
    # lets us get around this issue
    return shared_x, T.cast(shared_y, 'int32')

def exec_Prog() :
    
    #ref http://deeplearning.net/tutorial/gettingstarted.html
    # Load the dataset
    fname_In = "../data/mnist.pkl.gz"
    f = gzip.open(fname_In, 'rb')
#     f = gzip.open('mnist.pkl.gz', 'rb')

    #ref https://stackoverflow.com/questions/42940851/unicodedecodeerror-ascii-codec-cant-decode-byte-0x8b "answered Mar 22 '17 at 0:58"
    train_set, valid_set, test_set = cPickle.load(f, encoding='latin1')
    
#     train_set, valid_set, test_set = cPickle.load(f, encoding='utf-8')
            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x90 in position 614: invali
            # d start byte
#     train_set, valid_set, test_set = cPickle.load(f, encoding='utf-8')
#     train_set, valid_set, test_set = cPickle.load(f)

    #d.4,#2    
    test_set_x, test_set_y = shared_dataset(test_set)
    valid_set_x, valid_set_y = shared_dataset(valid_set)
    train_set_x, train_set_y = shared_dataset(train_set)
    
    batch_size = 500    # size of the minibatch
    
    # accessing the third minibatch of the training set
    
    data  = train_set_x[2 * batch_size: 3 * batch_size]
    label = train_set_y[2 * batch_size: 3 * batch_size]
    
    f.close()
    
    
    print ("[%s:%d] exec_Prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    
#/exec_Prog()

if __name__ == "__main__" :

    '''###################
        evecute        
    ###################'''
    exec_Prog()
    
    
    print
    print("[%s:%d] done" % (libs.thisfile(), libs.linenum()))
