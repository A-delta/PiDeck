from pideck import pi_config
from signal import pause


def main():
    pi = pi_config.Pi([
        {"pin": "21", "type_input": "button"},
        {"pin": "20", "type_input": "button"},
        {"pin": "16", "type_input": "button"},
    ])
    pause()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass