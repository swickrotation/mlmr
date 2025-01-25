import cv2
import numpy as np
import os
from  PIL import Image

def imagePreProcessor(inputFolder):
    for img in os.listdir(inputFolder):
        img = Image.open(img)
#        print(type(img))
        imgNorm = np.zeros((img.shape[0], img.shape[1]))
#        img = cv2.normalize(img, imgNorm, 0, 255, cv2.NORM_MINMAX)

imagePreProcessor('../trainingData/pagesAsImages')
