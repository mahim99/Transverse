# import os
# from google.cloud import translate_v2 as translate
# from google.cloud import speech_v1p1beta1 as speech
# from google.cloud.speech_v1p1beta1 import enums
# from google.cloud.speech_v1p1beta1 import types

# # set up the translation client
# translate_client = translate.Client()

# # set up the speech-to-text client
# client = speech.SpeechClient()

# # ask the user for the desired language
# target_language = input("Enter target language: ")

# # set up the recognition config
# config = types.RecognitionConfig(
#     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#     language_code='en-US')

# # start recording the user's speech
# os.system("rec --channels=1 --bits=16 --rate=16000 voice.wav trim 0 5")

# # read the recorded audio file
# with open("voice.wav", 'rb') as audio_file:
#     content = audio_file.read()

# # set up the recognition audio
# audio = types.RecognitionAudio(content=content)

# # perform speech-to-text recognition
# response = client.recognize(config, audio)

# # get the recognized text
# text = response.results[0].alternatives[0].transcript

# # translate the text to the target language
# translation = translate_client.translate(text, target_language=target_language)

# # print the translation
# print(f"Translation: {translation['translatedText']}")



# #2

# import speech_recognition as sr
# from googletrans import Translator

# # Ask the user for the desired language
# language = input("Enter the desired language: ")

# # Initialize the speech recognizer
# r = sr.Recognizer()

# # Start listening to the user's speech
# with sr.Microphone() as source:
#     print("Speak now...")
#     audio = r.listen(source)

# # Recognize the speech
# text = r.recognize_google(audio)

# # Translate the text into the desired language
# translator = Translator()
# translated_text = translator.translate(text, dest=language).text

# # Print the translated text
# print(translated_text)

#3

# import speech_recognition as sr
# from googletrans import Translator

# # Ask the user for the desired language
# language = input("Enter the desired language: ")

# # Initialize the speech recognizer
# r = sr.Recognizer()

# # Start listening to the user's speech
# with sr.Microphone() as source:
#     print("Speak now...")
#     audio = r.listen(source)

# # Recognize the speech
# text = r.recognize_google(audio, phrase_time_limit=None)

# # Translate the text into the desired language
# translator = Translator()
# translated_text = translator.translate(text, dest=language).text

# # Print the translated text
# print(translated_text)

#4

import speech_recognition as sr
from googletrans import Translator

# Ask the user for the desired language
language = input("Enter the desired language: ")

# Initialize the speech recognizer
r = sr.Recognizer()

# Start listening to the user's speech
with sr.Microphone() as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    # Keep listening until the user stops speaking for 1 second
    while True:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            break

# Recognize the speech
text = r.recognize_google(audio)

# Translate the text into the desired language
translator = Translator()
translated_text = translator.translate(text, dest=language).text

# Print the translated text
print(translated_text)