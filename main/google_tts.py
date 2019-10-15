import os

from gtts import gTTS


mytext = "GOOGLE TEXT TO SPEECH SYNTHESIS INITIATED"

def tts_online(mytext):

	try :
		speech = gTTS(text=mytext, lang='en', slow=False)
        
		speech.save("l.mp3")

		os.system("sudo mpg321 l.mp3")

		os.system("rm l.mp3")
	except :
		print("!!!!!!!!!!!!! Connection could not be establshed switching to OFFLINE mode ....wait")
		from py_tts import tts_offline
		tts_offline(mytext)
	
print("system online, google tts imported")
tts_online(mytext)
