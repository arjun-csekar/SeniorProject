# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:47 2018

@author: June
"""
import numpy as np

class noise:
    def denoise(array, height, width):
        tempData = array.copy()
        for k in range (height - 2):
            for j in range(width - 2):
                s1 = np.asarray([array[k][j:3+j], array[k+1][j:3+j], array[k+2][j:3+j]])
                s2 = s1.copy()
                s2 = s2.ravel()
                s2.sort()
                s1[1][1] = s2[4]
                tempData[k+1][j+1] = s2[4]
        
        return tempData