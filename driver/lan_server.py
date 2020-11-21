from flask import Flask

app = Flask(__name__)

@app.route('/')
def conf():
    return "<h1>test</h1>"