#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:49:57 2020

@author: mehmetsat
"""

import numpy as np

x=np.ones([1,2])


def sigmoid(x):
    """
    Compute the sigmoid function for the input here.
    Arguments:
    x -- A scalar or numpy array.
    Return:
    s -- sigmoid(x)
    """

    ### YOUR CODE HERE (~1 Line)
    
    s = np.exp(x) / (np.exp(x) + 1)

    ### END YOUR CODE

    return s 

indices = [0,1,2,3,4]
y = [x for x in indices if indices.index(x) != 2]
