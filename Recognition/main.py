# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:04:14 2018

@author: June
"""

from PIL import Image
import edge
import noise
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('data/image.png').convert('L')
im.save('data/greyscale-before.png')
width, height = im.size

data = np.asarray(im)
#data = np.pad(data, ((1,1),(1,1)), 'constant')
#print(data)
plt.matshow(data)
plt.show()

data2 = noise.noise.denoise(data, im.height, im. width)
img = Image.fromarray(data2)
img.save('data/greyscale-after.png')

plt.matshow(data2)
plt.show()

matrix_hor = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], np.int32)
matrix_ver = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.int32)
data3 = edge.edge.edgeDetection(data2, matrix_hor, matrix_ver, im.height, im.width)

plt.matshow(data3)
plt.show()

img2 = Image.fromarray(data3)
img2.save('data/edge.png')