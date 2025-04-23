# This Python script calls the Text-to-Speech service 
# on IBM Cloud
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

# Get API key and service URL from .env file
load_dotenv()
api_key = os.getenv('TTS_API_KEY')
service_url = os.getenv('TTS_SERVICE_URL')

def text_to_speech(text):
    authenticator = IAMAuthenticator(api_key)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url(service_url)
    
    response = text_to_speech.synthesize(
        voice='en-US_AllisonV3Voice',
        text=text,
        accept='audio/wav')

    audio_data = response.get_result().content

    # save the audio file to file
    with open('output.wav', 'wb') as f:
        f.write(audio_data)