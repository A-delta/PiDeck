# -*- coding: utf-8 -*-

"""
Build a web server to receive the PiDeck's requests.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def conf():
    return "<h1>test</h1>" # This is a test.