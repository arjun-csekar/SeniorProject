# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:47 2018

@author: June
"""
import numpy as np

class noise:
    def denoise(array, height, width):
        print("denoise")
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

    def smooth(array, height, width):
        print("smooth")
        tempData = array.copy()
        for k in range (height - 2):
            for j in range(width - 2):
                num = 0
                s1 = np.asarray([array[k][j:3+j], array[k+1][j:3+j], array[k+2][j:3+j]])
                s2 = s1.copy()
                s2 = s2.ravel()
                s2.sort()
                for i in s2:
                    num += i
                num /= 9
                tempData[k+1][j+1] = num
        
        return tempData

    def gaussian(array1):
        print("gaussian")
        gaussian_kernel = np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]], np.int32)
        
        arrayOne = array1.copy()
        tempData = arrayOne.copy()

        array = np.pad(arrayOne, ((2,2),(2,2)), 'constant')
        width = array.shape[0]
        height = array.shape[1]

        for k in range (width-4):
            for j in range(height-4):
                s1 = np.asarray([array[k][j:5+j], array[k+1][j:5+j], array[k+2][j:5+j], array[k+3][j:5+j], array[k+4][j:5+j]])
                s2 = s1.copy()
                num = np.dot(s2.ravel(), gaussian_kernel.ravel())/273
                tempData[k][j] = num
        
        return tempData
