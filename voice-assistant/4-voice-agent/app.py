from flask import Flask, render_template, request
import os, json

# call text_to_speech function we've created earlier
from tts import text_to_speech
from stt import speech_to_text
from processmsg import process_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print('processing speech-to-text')
    audio_binary = request.data
    text = speech_to_text(audio_binary)
    print('output=', text)
    return text
    
@app.route('/process-message', methods=['POST'])
def process_message_route():
    print('processing process_message')
    input_prompt = request.data
    
    inputJSON = json.loads(input_prompt)
    print('input prompt=', inputJSON.get("userMessage"))
    text = process_message(inputJSON.get("userMessage"))
    print('output=', text)
    return text

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_route():
    input = request.data
    inputJSON = json.loads(input)
    print('text-to-speech route: input_text:', inputJSON.get("message"))
    output = text_to_speech(inputJSON.get("message"))
    print('text-to-speech route: output:', output)
    return output

if __name__ == "__main__":
    app.run(debug=True)