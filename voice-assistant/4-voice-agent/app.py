from flask import Flask, render_template, request
import os

# call text_to_speech function we've created earlier
from tts import text_to_speech
from stt import speech_to_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    


if __name__ == "__main__":
    app.run(debug=True)