
import cv2 as cv
import glob

''' Dataset Kaggle https://www.kaggle.com/datasets/andrewmvd/car-plate-detection'''

sift = cv.SIFT_create()

# model = cv.imread('queries/matricule4.png',0)
# cv.imshow('image model',model)
# cv.waitKey(0)
# requet = cv.imread('License Plates/bbcac63e32bd8137_jpg.rf.ef4704b0ada4fbbf613143abf52f6f86.jpg',0)
# cv.imshow('image requet',requet)
# cv.waitKey(0)
model = [cv.imread(file) for file in glob.glob("C:/Users/Lina/Desktop/Sam/Progs/ProjetCV/queries/*.png")]
requet = [cv.imread(file) for file in glob.glob("C:/Users/Lina/Desktop/Sam/Progs/ProjetCV/License Plates/*.jpg")]


def SiftDetect(img):
    kp, des = sift.detectAndCompute(img, None)
    result = cv.drawKeypoints(img, kp, des)
    return result, kp, des

i = 0
for mod in model:
    i += 1
    j = 0
    img1, kp1, des1 = SiftDetect(mod)
    for req in requet:
        j += 1
        img2, kp2, des2 = SiftDetect(req)

        bf = cv.BFMatcher(cv.NORM_L2, crossCheck=False)
        Matches = bf.knnMatch(des2, des1, k=2)
        good = []
        for m, n in Matches:
            if m.distance < 0.3*n.distance:
                good.append([m])
        imgf = cv.drawMatchesKnn(req, kp2, mod, kp1, good, None, flags=2)
        if good != []:
            print("matricule "+str(i)+" voiture "+str(j)+" "+str(good))
            cv.imshow('image Final', imgf)
            cv.waitKey(1000)
    cv.destroyAllWindows()













