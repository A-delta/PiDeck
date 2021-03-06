class Mixin:

    def add_USB_Device(self, input_number):
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
            print(f"{term_fail}USB Device {input_number} doesn't exist. Skipped.{term_endc}")
            return
        self.usb_devices.append(usb)
        self.usb_channels.append(input_number)

        self.log(f"USB Device added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.usb_device_loop, args=(usb, input_number))
        usb_device_thread.start()

    def add_gamepad_device(self):
        usb_device_thread = Thread(name="Gamepad configuring", target=self.configure_gamepad)
        usb_device_thread.start()

    def configure_gamepad(self):
        from xbox360controller import Xbox360Controller

        self.has_gamepad = True

        try:
            with Xbox360Controller(raw_mode=True) as controller:
                print("configuring gamepad")
                for b in controller.buttons:
                    b.when_pressed = self.on_button_pressed

                for a in controller.axes:
                    a.when_moved = self.on_axis_moved_raw
                pause()
        except Exception as error:
            print(f"{term_fail}No USB Controller connected. Skipped. \nError : {error}{term_endc}")

    def on_button_pressed(self, button):
        self.log('Button {0} was pressed'.format(button.name))
        self.send_data({
            "code": self.code,

            "request": {
                "type": "Gamepad",
                "pin": '0',
                "value": button.name,
            }

        })

    def on_axis_moved_raw(self, axis):
        value = axis.value
        self.log(f"Axis {axis.name} moved to {value}")
        self.send_data({
            "code": self.code,

            "request": {
                "type": "Gamepad",
                "pin": '0',
                "value": axis.name,
                "extra": value
            }

        })

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