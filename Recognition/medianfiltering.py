# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 13:54:04 2018

@author: June
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('greyscale-after - Copy.png').convert('L')
im.save('greyscale-before.png')
width, height = im.size

data = np.asarray(im)
#data = np.pad(data, ((1,1),(1,1)), 'constant')
#print(data)
plt.matshow(data)
plt.show()

def denoise(array, height, width):
    tempData = array.copy()
    for k in range (height - 2):
        for j in range(width - 2):
            s1 = np.asarray([data[k][j:3+j], data[k+1][j:3+j], data[k+2][j:3+j]])
            s2 = s1.copy()
            s2 = s2.ravel()
            s2.sort()
            s1[1][1] = s2[4]
            tempData[k+1][j+1] = s2[4]
    
    return tempData

data2 = denoise(data, im.height, im. width)
img = Image.fromarray(data2)
img.save('greyscale-after.png')

plt.matshow(data2)
plt.show()

def edgeDetection(array, matrix_hor, matrix_ver, height, width):
    tempData = array.copy()
    tempData = np.pad(tempData, ((1,1),(1,1)), 'constant')
    num = 0
    
    for k in range (height - 2):
        for j in range(width - 2):
            s1 = np.asarray([data[k][j:3+j], data[k+1][j:3+j], data[k+2][j:3+j]])
            x = np.dot(s1.ravel(), matrix_hor.ravel())
            y = np.dot(s1.ravel(), matrix_ver.ravel())
            
            num = np.sqrt((x * x) + (y * y))
            tempData[k+1][j+1] = num
            
    return tempData

matrix_hor = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], np.int32)
matrix_ver = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.int32)
data3 = edgeDetection(data2, matrix_hor, matrix_ver, im.height, im.width)

plt.matshow(data3)
plt.show()

img2 = Image.fromarray(data3)
img2.save('edge.png')
