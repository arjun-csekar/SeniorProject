# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:04:14 2018

@author: June
"""

from PIL import Image
from edge import edge
from noise import noise
import numpy as np
import matplotlib.pyplot as plt
import cv2
from contour import contour

class main:

    def run(val, num, path, w, h, i):
        print(val)
        if(val == 1):
            main.noise_start(i)
            main.edge_start(num)
            main.fill_start()
            main.contour_start(path, w, h)
        elif(val == 2):
            main.edge_start(num)
            main.fill_start()
            main.contour_start(path, w, h)
        elif(val == 3):
            main.contour_start(path, w, h)

    def noise_start(i):
        print("noise")
        global data1
        if(i == 1):
            data1 = noise.denoise(data, im.height, im. width)
        elif(i == 2):
            data1 = noise.smooth(data, im.height, im. width)
        
        img = Image.fromarray(data1)
        img.save('data/greyscale-after.png')
        
    def edge_start(num):
        print("edge")
        global data2
        testing_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
        matrix_hor = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], np.int32)
        matrix_ver = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.int32)
        data2 = edge.edgeDetection(data1, matrix_hor, matrix_ver, im.height, im.width, num)
        img2 = Image.fromarray(data2)
        img2.save('data/edge.png')
        
    def fill_start():
        print("fill")
        im_floodfill = data2.copy()
        h, w = data2.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(im_floodfill, mask, (0,0), 255)
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)
        im_out = data2 | im_floodfill_inv

        img3 = Image.fromarray(im_out)

        img3.save('data/foreground.png')

    def contour_start(path, w, h):
        print("contour")
        data3 = contour.start_contour(path, w, h)
            
    def start_convert(index, e, path, w, h, i):
        global im
        global width
        global height
        global data
        
        im = Image.open(path).convert('L')
        im.save('data/greyscale-before.png')
        width, height = im.size

        data = np.asarray(im)

        main.run(index, e, path, w, h, i)

                  
'''
        data2 = noise.noise.denoise(data, im.height, im. width)
        img = Image.fromarray(data2)
        img.save('data/greyscale-after.png')

        testing_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
        matrix_hor = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], np.int32)
        matrix_ver = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.int32)
        data3 = edge.edge.edgeDetection(data2, matrix_hor, matrix_ver, im.height, im.width, 100)


        img2 = Image.fromarray(data3)
        img2.save('data/edge.png')


        im_floodfill = data3.copy()
        h, w = data3.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(im_floodfill, mask, (0,0), 255)
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)
        im_out = data3 | im_floodfill_inv

        img3 = Image.fromarray(im_out)

        img3.save('data/foreground.png')

        data4 = contour.contour.start_contour(path)
        

'''


