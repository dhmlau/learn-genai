# Voice assistant

- GPT-3: enable understanding and response
- Watson Embeddable AI: Speech-to-Text (STT) and Text-to-Speech (TTS)

Repo: https://github.com/arora-r/chatapp-with-voice-and-openai-outline.git


## Step 1: Text-to-Speech

First, create a [Text to speech service](https://cloud.ibm.com/catalog/services/text-to-speech) on [IBM Cloud](https://cloud.ibm.com/). A free/lite plan should be enough for learning purpose.

After the service is created, you can get the API key and service URL to call the service. 

To test your API key and service URL, you can run the following curl command:
```sh
curl -X POST -u "apikey:{apikey}" --header "Content-Type: application/json" --header "Accept: audio/wav" --data "{\"text\":\"hello world\"}" --output hello_world.wav "{url}/v1/synthesize?voice=en-US_MichaelV3Voice"
```
Replace `{apikey}` and `{url}` with the values you had. 
You can also select a different voice and language. For details, see [the tutorial](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-gettingStarted#getting-started-tutorial).


To run: 

1. Install `ibm-watson` python library
    ```ssh
    pip install ibm-watson
    ```

2. Set the environment variables `TTS_API_KEY` and `TTS_SERVICE_URL`. They are the API key and service URL for the Text-to-Speech service on IBM Cloud that was created previously. 

    ```ssh
    export TTS_API_KEY={your_api_key}
    export TTS_SERVICE_URL={your_service_url}
    ```

To check it's set properly:
    ```ssh
    echo $TTS_API_KEY
    ```

3. Run the Python script using the command below:
    ```ssh
    python3 1.tts.py
    ```

As a result, a file `output.wav` will be created in the same folder as `1-tts.py`. 

### Reference
- API Docs: https://cloud.ibm.com/apidocs/text-to-speech
- Python SDK: https://github.com/watson-developer-cloud/python-sdk


## Step 2: Speech-to-Text
First, create a [Speech-to-Text service](https://cloud.ibm.com/catalog/services/speech-to-text) on [IBM Cloud](https://cloud.ibm.com/).

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

## Step 3: OpenChat

As one of the labs in the course [Building Generative AI-Powered Applications with Python](https://www.coursera.org/learn/building-gen-ai-powered-applications/home/welcome), it suggested to use the `gpt-4` model from OpenAI. Unfortunately, I was not able to get it to run without paying extra credits. As a result, I'm switching to use `openchat/openchat-3.5-1210` model from HuggingFace. 


1. Install python libraries 
```
pip install transformers accelerate torch
```

### Reference
- OpenAI APIs are not being used in my app, but here are some references I've looked up:
    - OpenAI repo: https://github.com/openai/openai-python
    - OpenAI docs: https://platform.openai.com/docs/overview
    - Get API key: https://platform.openai.com/settings/organization/api-keys


## Step 4 - Putting everything together

```
pip install flask
```

Project layout:
```
my_project/
 |- app.py
 |- templates/
    |-- index.html

```
