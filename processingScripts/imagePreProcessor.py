import cv2
import numpy as np
import os
from  PIL import Image

'''
In order to make the OCR most effective, we need to pre-process the data. 
There are a few standard operations to perform, including re-sizing,
de-noising, thresholding , and grayscaling. We do all of this below.
'''

def imagePreProcessor(inputDir):

    #First we normalize the images:

    for img in os.listdir(inputDir):
        imgPath = os.path.join(inputDir, img)
        img = Image.open(imgPath)
        img = np.array(img)
#        print(img.shape)
        normImg = np.zeros((img.shape[0], img.shape[1]))
        img = cv2.normalize(img, normImg, 0, 255, cv2.NORM_MINMAX)


imagePreProcessor('../trainingData/testingDir')
