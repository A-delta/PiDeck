from pideck.pi import Pi
from subprocess import run
import subprocess


def wait_for_connection():
    run("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app".split())
    subprocess.check_output()


def main():
    pi = Pi([
        {"pin": "21", "type_input": "button"},
        {"pin": "20", "type_input": "button"},
        {"pin": "16", "type_input": "button"},
    ])

    pi.add_ADC_Device_PCF8591(2)
    pi.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass