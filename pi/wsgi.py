# -*- coding: utf-8 -*-

"""
Entrypoint to run the web server with Gunicorn.
"""

from connect_server import app

if __name__ == "__main__":
    app.run()