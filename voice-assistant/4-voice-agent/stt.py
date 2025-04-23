import os
from os.path import join, dirname
import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# audio_file: output.wav
def speech_to_text(audio_file):
    # Set up the authenticator
    api_key = os.getenv('STT_API_KEY')
    service_url = os.getenv('STT_SERVICE_URL')

    authenticator = IAMAuthenticator(api_key)
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(service_url)

    with open(join(dirname(__file__), './.', audio_file),
                'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            word_alternatives_threshold=0.9,
            keywords=['hello'],
            keywords_threshold=0.5
        ).get_result()

    #print(json.dumps(speech_recognition_results, indent=2))

    # For simplicity sake, we're leaving out the error checking for now
    transcript = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    return transcript