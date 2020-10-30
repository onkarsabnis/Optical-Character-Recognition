
import pytesseract
from PIL import Image
import re

##pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import tkinter as tk 
from tkinter import filedialog 
root = tk.Tk() 
root.withdraw() 
file_path = filedialog.askopenfilename() 

##print(file_path)

img = Image.open(file_path)

print(img)

text = pytesseract.image_to_string(img)   

with open('new_file.txt','w') as f :
	print ('Image text: \n ', text, file = f)

#### python .\OCR.py > img2_summary.txt ...this command can be used directly to generate o/p into a txt file


string = open('new_file.txt').read()
new_str = re.sub('[^a-zA-Z0-9/n/.]', ' ', string)
#new_str = [nstr.replace('[^a-zA-Z0-9/n/.]','\n') for nstr in new_str]
new_str = re.sub('[ \t\n]+', ' ', new_str)

with open('b.txt', 'w') as f:
	##print(new_str , "")
	open('b.txt', 'w').write(new_str)


"""
with open('file.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace('  ', '') for line in lines]

# finally, write lines in the file
with open('file.txt', 'w') as f:
    f.writelines(lines)


"""
