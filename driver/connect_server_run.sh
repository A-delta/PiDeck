#!/bin/sh

gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app