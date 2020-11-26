from pideck.pi_config import Pi


def main():
    pi = Pi([
        {"pin": "21", "type_input": "button"},
        {"pin": "20", "type_input": "button"},
        {"pin": "16", "type_input": "button"},
    ])

    pi.add_ADC_Device(2)
    pi.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass