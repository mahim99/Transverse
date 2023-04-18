from flask import Flask, render_template, request, redirect, url_for
import pytesseract
import os
from PIL import Image
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        # get the language input from the user
        language = request.form['language']

        # check if image file is uploaded
        if request.files:
            # get the uploaded image file
            image = request.files['image']
            # save the image file to the uploads directory
            image_path = os.path.join('uploads', image.filename)
            image.save(image_path)

            # use pytesseract library to extract text from image
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open(image_path), lang=language)

            # delete the uploaded image file
            os.remove(image_path)

            # render the translated text to user
            return render_template('result.html', text=text)

        else:
            # if no image file is uploaded, redirect to homepage
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
