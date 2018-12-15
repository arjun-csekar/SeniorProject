from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2
import math
from scipy import ndimage
import glob
import keras
import re

class recognition:
    def getBestShift(img):
        cy,cx = ndimage.measurements.center_of_mass(img)

        rows,cols = img.shape
        shiftx = np.round(cols/2.0-cx).astype(int)
        shifty = np.round(rows/2.0-cy).astype(int)

        return shiftx,shifty


    def shift(img,sx,sy):
        rows,cols = img.shape
        M = np.float32([[1,0,sx],[0,1,sy]])
        shifted = cv2.warpAffine(img,M,(cols,rows))
        return shifted

    def recognize():
        
        letters = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
        10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
        20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: '-'}

        #images = [cv2.imread(file, 0) for file in glob.glob('letters/*.png')]
        images = glob.iglob('data/Extract/*.png')
        images = sorted(images, key=lambda x:float(re.findall("(\d+)",x)[0]))
            
        img_width, img_height = 28, 28

        model = load_model('emnist_cnn_model.h5')
        model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

        k = 1
        string = ""
        for gray in images:
            gray = cv2.imread(gray, 0)
            #gray = cv2.imread("2.png", 0)

            # rescale it
            gray = cv2.resize(255-gray, (28, 28))
            # better black and white version
            (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            while np.sum(gray[0]) == 0:
                gray = gray[1:]

            while np.sum(gray[:,0]) == 0:
                gray = np.delete(gray,0,1)

            while np.sum(gray[-1]) == 0:
                gray = gray[:-1]

            while np.sum(gray[:,-1]) == 0:
                gray = np.delete(gray,-1,1)

            rows,cols = gray.shape

            if rows > cols:
                factor = 20.0/rows
                rows = 20
                cols = int(round(cols*factor))
                # first cols than rows
                gray = cv2.resize(gray, (cols,rows))
            else:
                factor = 20.0/cols
                cols = 20
                rows = int(round(rows*factor))
                # first cols than rows
                gray = cv2.resize(gray, (cols, rows))

            colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
            rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
            gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

            shiftx,shifty = recognition.getBestShift(gray)
            shifted = recognition.shift(gray,shiftx,shifty)
            gray = shifted

            # save the processed images
            cv2.imwrite("processed.png", gray)
            #cv2.imwrite("out\\"+str(k)+".png", gray)

            #img = image.load_img('processed.png', target_size=(img_width, img_height))
            #img = img.shape((28, 28,1))
            #x = image.img_to_array(img)
            file = cv2.imread('processed.png') 
            file = cv2.resize(file, (28, 28))
            file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            file = file.reshape((28, 28, 1))
            x = np.expand_dims(file, axis=0)
            predictions = model.predict(x)
            if(letters[(np.argmax(predictions))] == 'q'):
                string = string + "_"
            else:
                string = string + letters[(np.argmax(predictions))]
                #print(letters[(np.argmax(predictions))])
            k = k + 1
        print(string)
        return string
        #images = np.vstack([x])
        #classes = model.predict_classes(images, batch_size=10)
        #print (classes)
