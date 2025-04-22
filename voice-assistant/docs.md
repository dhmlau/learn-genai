# Voice assistant

- GPT-3: enable understanding and response
- Watson Embeddable AI: Speech-to-Text (STT) and Text-to-Speech (TTS)

Repo: https://github.com/arora-r/chatapp-with-voice-and-openai-outline.git


## Text-to-Speech

Create a Text to speech service on IBM Cloud, with a free plan.
You'll get a API key and URL to call the service. 


```sh
curl -X POST -u "apikey:{apikey}" --header "Content-Type: application/json" --header "Accept: audio/wav" --data "{\"text\":\"hello world\"}" --output hello_world.wav "{url}/v1/synthesize?voice=en-US_MichaelV3Voice"
```
Replace `{apikey}` and `{url}` with the values you had. 
You can also select a different voice and language. For details, see[the tutorial](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-gettingStarted#getting-started-tutorial).

API Docs: https://cloud.ibm.com/apidocs/text-to-speech
Python SDK: https://github.com/watson-developer-cloud/python-sdk


Install `ibm-watson` python library
```
pip install ibm-watson
```

# Speech-to-Text
Create Speech-to-Text service on IBM Cloud

API Docs: https://cloud.ibm.com/apidocs/speech-to-text
