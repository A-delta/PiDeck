# 2021 RaspiMote
# https://github.com/RaspiMote

from pi.pi import Pi


def main():
    """
    This file is a template for your main.py that will be running on your Raspberry Pi.
    It is an example of minimal code that adds various devices to be read by the Pi.
    Please read docstrings before using a method from the Pi class.
    """

    driver_computer_ip = "192.168.1.16"  # IP example
    pi = Pi(driver_computer_ip, "WiFi")        # Create Pi object (WiFi only for now)

    pi.add_buttons_configuration([{"pin": "21", "type_input": "button"}])  # Add a button on GPIO 21

    pi.add_USB_Device(1)
    """
    Add a USB Device, see https://github.com/RaspiMote/RaspiMote/blob/main/utility/identify_usb_device.py
    to know which number you must write.
    """

    pi.establish_connection()  # Create connection and get connection code from Driver on your computer


if __name__ == "__main__":
    main()
