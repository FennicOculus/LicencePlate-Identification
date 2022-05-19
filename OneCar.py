import cv2 as cv
import glob
import Functions
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames()
print(files[0])
voiture = cv.imread(str(files[0]),0)
cv.imshow('image requet',voiture)

plaques = [cv.imread(file) for file in glob.glob("C:/Users/Lina/Desktop/Sam/Progs/ProjetCV/queries/*.png")]
sift = cv.SIFT_create()
found = 0
for plaque in plaques:
    img1, kp1, des1 = Functions.SiftDetect(plaque, sift)

    img2, kp2, des2 = Functions.SiftDetect(voiture, sift)

    bf = cv.BFMatcher(cv.NORM_L2, crossCheck=False)
    Matches = bf.knnMatch(des2, des1, k=2)
    good = []
    for m, n in Matches:
        if m.distance < 0.3 * n.distance:
            good.append([m])
    imgf = cv.drawMatchesKnn(voiture, kp2, plaque, kp1, good, None, flags=2)
    if good != []:
        found = 1
        print("Voiture Trouvé")
        cv.imshow('image Final', imgf)
        cv.waitKey(1000)
if found == 0:
    print("NOT FOUND")
cv.destroyAllWindows()
