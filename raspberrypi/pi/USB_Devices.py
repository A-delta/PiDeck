from threading import Thread


class Mixin:
    def add_USB_Device(self, input_number, device_name):
        """
        Add one or multiple USB devices, such as mouses (buttons) or keyboards.
        input_number can be found by running the provided script : /utility/identify_usb_device.py

        :param input_number: Number found by running the script. Also event number in /dev/input/ on UNIX systems.
        :return:
        """
        from evdev import InputDevice
        try:
            usb = InputDevice(f"/dev/input/event{input_number}")
        except:
            print(f"{self.term_fail}USB Device {input_number} doesn't exist. Skipped.{self.term_endc}")
            return
        self.usb_devices.append(device_name)
        self.usb_channels.append(input_number)

        self.log(f"USB Device added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.usb_device_loop, args=(usb, input_number))
        usb_device_thread.start()

    def usb_device_loop(self, usb, input_number):
        from evdev import categorize, ecodes

        for event in usb.read_loop():
            if event.type == ecodes.EV_KEY:
                self.send_data({
                    "code": self.code,

                    "request": {
                        "type": "USB",
                        "pin": input_number,
                        "value": ecodes.KEY[event.code],
                        "extra": event.value
                    }

                })

                self.log(categorize(event))

