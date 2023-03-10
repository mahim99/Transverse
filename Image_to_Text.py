from PIL import Image
import pytesseract

dire=input("Type full path to image you want to convert to text:")
im = Image.open(dire)

language=input("ENG")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(im, lang=language)
filename=input("Type output file name:")
file1 = open(filename+"-"+language+".txt","w")
file1.write(text)
file1.close()
print("Done...") 