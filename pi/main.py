from raspimote.pi import Pi
from sys import argv
from subprocess import run
import subprocess


def main(argv):
    if "-verbose" in argv or '-v' in argv:
        verbose = True
    else:
        verbose = False

    pi = Pi([
        {"pin": "21", "type_input": "button"},
        {"pin": "20", "type_input": "button"},
        {"pin": "16", "type_input": "button"},
        {"pin": "6", "type_input": "button"},
        {"pin": "13", "type_input": "button"},
        {"pin": "19", "type_input": "button"},
        {"pin": "26", "type_input": "button"},
    ], verbose)

    pi.add_ADC_Device_PCF8591(2)
    pi.establish_connection()
    pi.run()


if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass