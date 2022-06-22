import cv2 as cv
import glob
import Functions
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

def reco():
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames(initialdir='License Plates/', title='Selectionnez La Voiture')
    if files:
        voiture = cv.imread(str(files[0]))

        plaques = [cv.imread(file) for file in glob.glob("DataBase/*.png")]
        sift = cv.SIFT_create()
        found = 0
        img2, kp2, des2 = Functions.SiftDetect(voiture, sift)
        for plaque in plaques:
            img1, kp1, des1 = Functions.SiftDetect(plaque, sift)

            bf = cv.BFMatcher(cv.NORM_L2, crossCheck=False)
            Matches = bf.knnMatch(des2, des1, k=2)
            good = []
            for m, n in Matches:
                if m.distance < 0.3 * n.distance:
                    good.append([m])
            imgf = cv.drawMatchesKnn(voiture, kp2, plaque, kp1, good, None, flags=2)
            #cv.imshow('test', imgf)
            #cv.waitKey(0)
            if good != []:
                found = 1
                tkinter.messagebox.showinfo("Response", "This car belong to our parking lot")
                cv.imshow('image Final', voiture)
                cv.waitKey(0)
                return
                
        if found == 0:
            tkinter.messagebox.showinfo("Response", "Not Found, This car does NOT belong to our parking lot")
        cv.destroyAllWindows()
    root.destroy()
