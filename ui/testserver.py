from flask import Flask, request
from flask_cors import CORS
from json import loads
from waitress import serve

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello():
    print(type(loads(list(request.form.to_dict().keys())[0])))
    return "This is a response."


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=12345)