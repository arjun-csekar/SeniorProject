# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:03:47 2018

@author: June
"""
import numpy as np
import cv2 as cv
from PIL import Image
import os

class contour:
    def sort_contours(cnts, method="left-to-right"):
        reverse = False
        i = 0
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1
        boundingBoxes = [cv.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][i], reverse=reverse))
        return cnts

    def start_contour(path, wi, he):
        dirPath = "data/Extract"
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath+"/"+fileName)
            
        print("start_contour")
        im = cv.imread('data/edge.png')
        im2 = cv.imread(path)
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        data = np.asarray(imgray)
        _, contours, _ = cv.findContours(data, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        i = 0 
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            if(h >= he and h < im.shape[1] and w >= wi and w < im.shape[0]):
                cv.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 1)
                imgRect = im2[y:y+h,x:x+w]
                extract = Image.fromarray(imgRect)
                extract.save('data/Extract/' + str(i) + '.png')
            i += 1

        img = Image.fromarray(im)
        img.save('data/contour.png')
