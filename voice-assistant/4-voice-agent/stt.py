import os
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
api_key = os.getenv('STT_API_KEY')
service_url = os.getenv('STT_SERVICE_URL')

def speech_to_text(audio_binary):
    # Set up the authenticator
    authenticator = IAMAuthenticator(api_key)
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(service_url)

    speech_recognition_results = speech_to_text.recognize(
        audio=audio_binary
    ).get_result()

    # For simplicity sake, we're leaving out the error checking for now
    transcript = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    return transcript