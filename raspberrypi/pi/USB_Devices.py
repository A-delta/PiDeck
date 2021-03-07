from threading import Thread


class Mixin:
    def add_generic_USB_device(self, input_number, device_name):
        from evdev import InputDevice
        try:
            usb = InputDevice(f"/dev/input/event{input_number}")
        except Exception:
            print(f"{self.term_fail}USB Device {input_number} doesn't exist. Skipped.{self.term_endc}")
            return
        self.usb_devices.append(device_name)
        self.usb_channels.append(input_number)

        self.log(f"USB Device added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.generic_usb_device_loop, args=(usb, device_name))
        usb_device_thread.start()

    def generic_usb_device_loop(self, usb, device_name):
        from evdev import categorize, ecodes

        for event in usb.read_loop():
            try:

                self.send_data(["USB", f"generic_usb_{device_name}", list(ecodes.ecodes)[list(ecodes.ecodes.values()).index(event.code)], event.value])

            except Exception as error:
                print(error)
                print("during USB (need debug)")

    def add_USB_mouse(self, input_number):
        from evdev import InputDevice

        try:
            USB_mouse = InputDevice(f"/dev/input/event{input_number}")

        except Exception:
            print(f"{self.term_fail}USB Device {input_number} doesn't exist. Skipped.{self.term_endc}")
            return

        self.usb_devices.append(f"mouse_{input_number}")
        self.log(f"USB Mouse added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.usb_mouse_read_events, args=(USB_mouse, input_number))
        usb_device_thread.start()

    def add_USB_keyboard(self, input_number):
        from evdev import InputDevice

        try:
            USB_keyboard = InputDevice(f"/dev/input/event{input_number}")
        except Exception:
            print(f"{self.term_fail}USB Device {input_number} doesn't exist. Skipped.{self.term_endc}")
            return

        self.usb_devices.append(f"keyboard_{input_number}")
        self.log(f"USB Mouse added with input{input_number}")

        usb_device_thread = Thread(name="USB Device Reading", target=self.usb_keyboard_read_events, args=(USB_keyboard, input_number))
        usb_device_thread.start()

    def usb_mouse_read_events(self, mouse, input_number):
        from evdev import categorize, ecodes

        for event in mouse.read_loop():

            if event.code == 8:
                self.send_data(("USB", f"mouse_{input_number}", "scroll", event.value))

            elif event.code <= 1:
                self.send_data(("USB", f"mouse_{input_number}", ecodes.REL[event.code], event.value))

            else:
                try:
                    self.send_data(("USB", f"mouse_{input_number}", ecodes.BTN[event.code], event.value))
                except Exception as error:
                    print(error)
                    print(self.term_fail, "not supported for the moment :", event.code, self.term_endc)


    def usb_keyboard_read_events(self, keyboard, input_number):
        from evdev import categorize, ecodes

        for event in keyboard.read_loop():
            if event.type == ecodes.EV_KEY:
                self.send_data(("USB", f"keyboard_{input_number}", ecodes.KEY[event.code], event.value))
                self.log(f"{categorize(event)}")
