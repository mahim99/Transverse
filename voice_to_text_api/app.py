from flask import Flask, request, render_template
import os
import speech_recognition as sr
from googletrans import Translator

app = Flask(__name__)

# Set up Google Translate client
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get audio from user's microphone using SpeechRecognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Get target language from form data
    target_language = request.form['target_language']

    # Convert audio to text using SpeechRecognition
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Error: Unable to recognize speech."
    except sr.RequestError:
        return "Error: Speech recognition request failed."

    # Translate text to target language using Google Translate
    try:
        translated_text = translator.translate(text, dest=target_language).text
    except ValueError:
        return "Error: Invalid target language code."

    return translated_text

if __name__ == '__main__':
    app.run(debug=True)
