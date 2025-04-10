# Building chatbot

## Pre-requisite
1. install Flask
```
pip install flask
```

2. install python libraries

```
pip install transformers torch
```

## Stage 1: Build a simple chatbot with fixed input

Build a simple terminal-based chatbot using [Facebook's blenderbot model](https://huggingface.co/facebook/blenderbot-400M-distill) and `transformers` python library from Hugging Face.

To run: 
```
python3 1-chatbot.py
```

Since the input is already specified, you'll see the output look like below: 
```
Input: {'input_ids': tensor([[1710,   86,   19,  544,  366,  304,  929,   38]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1]])}
Output: tensor([[   1,  281,  476,  929,  731,   21,  281,  632,  929,  712,  731,   21,
          855,  366,  304,   38,  946,  304,  360,  463, 5459, 7930,   38,    2,
            2]])
Decoded output: I'm doing well. I am doing very well. How are you? Do you have any hobbies?
Conversation history: ['hello, how are you doing?', "I'm doing well. I am doing very well. How are you? Do you have any hobbies?"]
```

_Note: You can move to the next step directly if you're familiar with the code. I just created this extra step to make sure everything is running without any inputs first._

## Stage 2: Build a simple chatbot that receives inputs from terminal
Similar to [previous app](./1-chatbot.py), except this one accepts inputs.


## Stage 3: Create a simple web app using Flask

_Optional: If you're familiar with Flask, you can skip this step._

**Pre-requisite**

Install the following python packages:
```
pip install flask
pip install flask_cors
```

By default, if the Flask app file name is `app.py`, then you can simply run `flask run`. In this repo, the file name is `3-app.py`, therefore, we need to set the `FLASK_APP` variable first, i.e. 


```sh 
$ export FLASK_APP=myapp.py
$ flask run
```

From a browser, go to http://127.0.0.1:5000.
