

#https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py#L4

import json
import requests


def ocr_online(filename = "image_1.png", overlay=False, api_key='97380cc56988957', language='eng'):

    try :    
        payload = {'isOverlayRequired': overlay,
                   'apikey': api_key,
                   'language': language,
                   }
        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={filename: f},
                              data=payload,
                              )
        test_file = r.content.decode()

        json_data = json.loads(test_file) # parses json data returned from ocr.space api
        print(json_data)
        data = json_data["ParsedResults"] # returns a list


        data = data[0] #returns a dictionary
        print(data["ParsedText"])
        print(type(data))
        return data["ParsedText"]
    except :
        print("!!!!!!!!!!! ocr.sapce couldn't be contacted switching to pytesseract .....wait")
        from tesseract_ocr import ocr_offline
        text = ocr_offline(filename)

print("ocr api imported")

