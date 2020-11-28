from pideck.pi import Pi
from sys import argv
from subprocess import run
import subprocess


def wait_for_connection():
    run("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app".split())
    subprocess.check_output()


def main(argv):
    if "verbose" in argv or 'v' in argv:
        verbose = True
    else:
        verbose = False

    pi = Pi([
        {"pin": "21", "type_input": "button"},
        {"pin": "20", "type_input": "button"},
        {"pin": "16", "type_input": "button"},
    ], verbose)

    pi.add_ADC_Device_PCF8591(2)
    pi.run()


if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass