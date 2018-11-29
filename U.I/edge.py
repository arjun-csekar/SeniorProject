# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:00 2018

@author: June
"""
import numpy as np

class edge:
    def edgeDetection(array, matrix_hor, matrix_ver, height, width, limit):
        tempData = array.copy()
        tempData = np.pad(tempData, ((1,1),(1,1)), 'constant')
        num = 0
        
        
        for k in range (height - 2):
            for j in range(width - 2):
                s1 = np.asarray([array[k][j:3+j], array[k+1][j:3+j], array[k+2][j:3+j]])
                x = np.dot(s1.ravel(), matrix_hor.ravel())
                y = np.dot(s1.ravel(), matrix_ver.ravel())
                
                num = np.sqrt((x * x) + (y * y))
                
                if(num > limit):
                    tempData[k+1][j+1] = 255
                else:
                    tempData[k+1][j+1] = 0
        
        return tempData
