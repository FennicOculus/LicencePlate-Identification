from skimage.segmentation import clear_border
import numpy as np
import imutils
import cv2

image = cv2.imread('License Plates/b1a50a3824887ee2_jpg.rf.68a4fd34fce20184287592f2680f895b.jpg', 0)
blur = cv2.GaussianBlur(image,(5,5),0)

(thresh, im_bw) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(thresh)
im_bw = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('test', im_bw)
cv2.waitKey(0)
