from threading import Thread
from signal import pause


class Mixin:
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
            print(f"{self.term_fail}No USB Controller connected. Skipped. \nError : {error}{self.term_endc}")

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
