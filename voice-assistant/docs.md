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

To run: 

1. Install `ibm-watson` python library
    ```
    pip install ibm-watson
    ```

2. Set the environment variables `TTS_API_KEY` and `TTS_SERVICE_URL`. They are the API key and service URL for the Text-to-Speech service on IBM Cloud that was created previously. 

3. Run the Python script using the command below:
```
python3 1.tts.py
```

As a result, a file `output.wav` will be created in the same folder as `1-tts.py`. 

## Speech-to-Text
Create Speech-to-Text service on IBM Cloud

To run:
1. Set the environment variables `STT_API_KEY` and `STT_SERVICE_URL` 
2. Run the following command:
```
python3 2-stt.py
```

The output looks like: 
```
python3 2-stt.py
{
  "result_index": 0,
  "results": [
    {
      "final": true,
      "alternatives": [
        {
          "transcript": "hello world ",
          "confidence": 0.99
        }
      ],
      "word_alternatives": [
        {
          "start_time": 0.0,
          "end_time": 0.33,
          "alternatives": [
            {
              "word": "hello",
              "confidence": 1.0
            }
          ]
        },
        {
          "start_time": 0.33,
          "end_time": 0.81,
          "alternatives": [
            {
              "word": "world",
              "confidence": 0.96
            }
          ]
        }
      ],
      "keywords_result": {
        "hello": [
          {
            "start_time": 0.0,
            "end_time": 0.33,
            "confidence": 1.0,
            "normalized_text": "hello"
          }
        ]
      }
    }
  ]
}
```

API Docs: https://cloud.ibm.com/apidocs/speech-to-text
