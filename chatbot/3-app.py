from flask import Flask

# add CORS
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/bananas')
def bananas():
    return 'This page has bananas!'

@app.route('/bread')
def bread():
    return 'This page has bread!'