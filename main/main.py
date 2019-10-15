import sys
from image_process import img_syn
from trash_kicker import delImg
from net_test import is_online

vid_path = "sampleVid.mp4"
name = "image_1.png"

if len(sys.argv) > 1 :
    ip = sys.argv[1]
    vid_path = "rtsp://"+ip+":8080/video/h264"
 
img_syn(vid_path)

if is_online() : # when pi is connected to internet
	print ("<<<<<<<<<<<<<<<<<<<<<<<<<< SYSTEM ONLINE >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	#from tesseract_ocr import ocr_offline
	from ocr_api import ocr_online
	from google_tts import tts_online
	text = ocr_online(name) # using ocr.space instead of pytesseract
	tts_online(text)        #using gtts
else : # when pi is not connected to internet
	print ("<<<<<<<<<<<<<<<<<<<<<<<<<< SYSTEM OFFLINE >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	from tesseract_ocr import ocr_offline
	from py_tts import tts_offline
	text = ocr_offline(name)
	tts_offline(text)


delImg()
