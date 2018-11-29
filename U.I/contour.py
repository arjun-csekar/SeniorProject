# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:47 2018

@author: June
"""
import numpy as np
import cv2 as cv
from PIL import Image

class contour:
    def start_contour(path, wi, he):
        im = cv.imread('data/foreground.png')
        im2 = cv.imread(path)
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        data = np.asarray(imgray)
        _, contours, _ = cv.findContours(data, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        i = 0 
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            #print(x, " ", y, " ", w, " ", h)
            if(h >= he and w >= wi):
                cv.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv.drawContours(im, contours, 0, (0,255,0), 1)
            #imgRect = im[y:y+h,x:x+w]
            #if(h >= he and w >= wi):
                imgRect = im2[y:y+h,x:x+w]
                extract = Image.fromarray(imgRect)
                #extract.save('data/Extract/' + str(i) + '.png')
            i += 1

        img = Image.fromarray(im)
        img.save('data/contour.png')
