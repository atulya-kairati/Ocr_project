import cv2

vid_path = "sampleVid.mp4" 

def read_img(vid_path) :
    cap = cv2.VideoCapture(vid_path)

    counter = 0
    imageCounter = 1

    while cap.isOpened() :
        ret, frame = cap.read()
        if ret :

            if (counter % 10) == 0 :
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite("image_"+str(imageCounter)+".png", gray)
                
                if imageCounter == 1 :    break #we need only one image
                
                imageCounter += 1
            counter += 1

        else :  break

print("image reader imported")
