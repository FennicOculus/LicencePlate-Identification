import cv2
from Functions import NameGeneration
from tkinter import filedialog, messagebox
from tkinter import *
import os

''' Dataset Kaggle https://www.kaggle.com/datasets/andrewmvd/car-plate-detection'''
'''https://www.section.io/engineering-education/license-plate-detection-and-recognition-using-opencv-and-pytesseract/'''

def Seg():

    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(initialdir='New Cars/', title='Ajout d\'une voiture')
    if not files:
        root.destroy()
        return
    #showing the original Image
    image = cv2.imread(str(files[0]))

    #Converting it to  gray Scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Reducing the noise
    gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

    edged = cv2.Canny(gray_image, 200, 300)

    cnts,_ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1=image.copy()
    cv2.drawContours(image1,cnts,-1,(0,255,0),3)

    cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
    screenCnt = None
    image2 = image.copy()
    cv2.drawContours(image2,cnts,-1,(0,255,0),3)
    name = NameGeneration('DataBase/*.png')

    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
            x,y,w,h = cv2.boundingRect(c) 
            new_img=image[y:y+h,x:x+w]
            cv2.imshow("test", new_img)
            cv2.waitKey(0)
            MsgBox = messagebox.askquestion ('Save','Do you want to save this image ?',icon = 'warning')
            if MsgBox == 'yes':
                cv2.imwrite('DataBase/'+str(name)+'.png',new_img)
                os.remove(files[0])
            else:
                messagebox.showinfo('Return','Image hasn\'t been saved')
            break
    root.destroy()
