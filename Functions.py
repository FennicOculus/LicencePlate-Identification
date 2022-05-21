import cv2
import glob
import os
import numpy as np
import datetime

def SiftDetect(img, sift):
    kp, des = sift.detectAndCompute(img, None)
    result = cv2.drawKeypoints(img, kp, des)
    return result, kp, des

def NameGeneration(directory):
    current_date = datetime.datetime.now()
    np.random.seed(int(current_date.strftime("%Y%m%d%H%M%S"))%2**10)
    hex_number = str(hex(np.random.randint(1677721588)))
    names = [file for file in glob.glob(str(directory))]
    for i in names:
        fName = os.path.basename(str(i))
        if hex_number == fName:
            return NameGeneration()
    return hex_number

