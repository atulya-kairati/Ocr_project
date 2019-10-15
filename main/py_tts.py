# sudo apt install espeak python3-espeak speech-dispatcher-espeak run this before using this program

import os

def tts_offline(text):
	os.system('espeak -w out.wav "{0}" && aplay out.wav'.format(text))

print("py tts through espeak imported")
tts_offline("System is offline, rudamentary text to speech  synthesis initiated")
