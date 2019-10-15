from gray_image_reader import read_img
from image_rotator import portrait
#from denoise import denoise
#from alpha_channel import alfaOff 
from trash_kicker import delImg 

vid_path = "sampleVid.mp4"

def img_syn(vid_path) :
    
    try :
        read_img(vid_path)
        portrait()
        print("Image read Successfully")
    except :
        print ("Image could not be read")
        exit()

print ("image process imported")
