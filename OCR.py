
import pytesseract
from PIL import Image

##pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


img = Image.open('img2.png')

print(img)

text = pytesseract.image_to_string(img)   

with open('new_file.txt','w') as f :
	print ('Image text:', text, file = f)

####python .\OCR.py > img2_summary.txt ...this command can be used directly to generate o/p into a txt file

