#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:52:00 2020

@author: mehmetsat
"""
import numpy as np

b = np.array([[8,1,7], [4,3,9], [5,2,6]])
np.apply_along_axis(b, 1, b)
print(b)