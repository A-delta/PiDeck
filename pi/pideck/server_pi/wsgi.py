# -*- coding: utf-8 -*-

"""
Entrypoint to run the web server with Gunicorn.
"""
from os import getpid
from connect_server import run

if __name__ == "__main__":

    run(getpid())