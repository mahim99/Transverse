from flask import Flask, render_template, request
from googletrans import Translator
from flask import jsonify

response = ''

app = Flask(__name__)
@app.route('/api')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():

    global response

    if (request.method == 'POST'):
        text = request.form['text']
        target_language = request.form['language']
        # Create a Translator object
        translator = Translator()
        # Translate the entered text to the desired language
        translated_text = translator.translate(text, dest=target_language)
        # Create a dictionary to hold the translated text
        response = {'translated_text': translated_text.text}
        # Return the response in JSON format
        return jsonify(response)
    else:
        return 'Error: Invalid request'
    
if __name__ == '__main__':
    app.run(debug=True)
