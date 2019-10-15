import os
import cv2

def portrait() :
    for i in range(1, 2) : # doing for image_1.png only
        img = cv2.imread("image_"+str(i)+".png",0)
        shape = img.shape
        hieght = shape[0]
        width = shape[1]

        if hieght < width :
            os.system("mogrify -rotate 90 " + "image_"+str(i)+".png")

print("image rotator imported")
