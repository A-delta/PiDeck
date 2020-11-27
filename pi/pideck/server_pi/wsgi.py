# -*- coding: utf-8 -*-

"""
Entrypoint to run the web server with Gunicorn.
"""

from connect_server import app
from os import getpid

class Test:
    def __init__(self):
        self.pid = getpid()

if __name__ == "__main__":
    app.run()