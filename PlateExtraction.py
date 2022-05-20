# Import packages
import cv2
import numpy as np
import random
import glob
from Functions import NameGeneration
from tkinter import filedialog
import os
from tkinter import *
import tkinter.messagebox
    
def mouseHandler(event,x,y,flags,param):
    global im_temp, pts_src

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(im_temp,(x,y),3,(0,255,255),5,cv2.LINE_AA)
        cv2.imshow("Image", im_temp)
        if len(pts_src) < 4:
        	pts_src = np.append(pts_src,[(x,y)],axis=0)

def addCar():
    global im_temp, pts_src
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(initialdir='New Cars/', title='Ajout d\'une voiture')
    
    if not files:
        root.destroy()
        return
    im_src = cv2.imread(str(files[0]))
                
    # Destination image
    height, width = 100, 300
    im_dst = np.zeros((height,width,3),dtype=np.uint8)

    # Create a list of points.
    pts_dst = np.empty((0,2))
    pts_dst = np.append(pts_dst, [(0,0)], axis=0)
    pts_dst = np.append(pts_dst, [(width-1,0)], axis=0)
    pts_dst = np.append(pts_dst, [(width-1,height-1)], axis=0)
    pts_dst = np.append(pts_dst, [(0,height-1)], axis=0)

    # Create a window
    cv2.namedWindow("Image", 1)
    im_temp = im_src
    pts_src = np.empty((0,2))
    cv2.setMouseCallback("Image",mouseHandler)
    cv2.imshow("Image", im_temp)
    cv2.waitKey(0)
    cropped_image = im_temp[int(pts_src[0,1]):int(pts_src[2, 1]), int(pts_src[0, 0]):int(pts_src[1, 0])]
        
    name = NameGeneration('C:/Users/Lina/Desktop/Sam/Progs/ProjetCV/DataBase/*.jpg')
    #cv2.imshow("Image last", im_dst)
    cv2.imwrite("DataBase/"+str(name)+".png", cropped_image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    tkinter.messagebox.showinfo("Response", "A new Licence Plate have been added to the database")
    MsgBox = tkinter.messagebox.askquestion ('Warning','Do you want to DELETE this image ?',icon = 'warning')
    if MsgBox == 'yes':
        tkinter.messagebox.showinfo('END','Image DELETED')
        os.remove(files[0])
    else:
        tkinter.messagebox.showinfo('Return','Image Kept')
    root.destroy()
        