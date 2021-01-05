from flask import Flask, request
from json import loads

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    print(loads(list(request.form.to_dict().keys())[0]))
    return "sth"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)