import pytesseract 
from PIL import Image

def ocr_offline(name):
	image = Image.open(name)

	text = pytesseract.image_to_string(image)

	print(text)

	return text

print("tesseract ocr imported")
