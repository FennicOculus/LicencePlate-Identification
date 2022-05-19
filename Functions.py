import cv2 as cv

def SiftDetect(img, sift):
    kp, des = sift.detectAndCompute(img, None)
    result = cv.drawKeypoints(img, kp, des)
    return result, kp, des