from threading import Thread
from signal import pause


class Mixin:
    def add_gamepad_device(self, controllers_number=1):

        for index in range(controllers_number):
            usb_device_thread = Thread(name="Gamepad configuring", target=self.configure_gamepad, args=[index])
            usb_device_thread.start()

    def configure_gamepad(self, index):
        from xbox360controller import Xbox360Controller
        self.gamepads.append([])
        try:
            with Xbox360Controller(index, raw_mode=True) as controller:
                self.log("configuring gamepad", index)
                for b in controller.buttons:
                    b.when_pressed = self.on_button_pressed
                    self.gamepads[index].append(b)

                for a in controller.axes:
                    a.when_moved = self.on_axis_moved_raw
                    self.gamepads[index].append(a)

                pause()

        except Exception as error:
            print(f"{self.term_fail}No USB Controller connected. Skipped. \nError : {error}{self.term_endc}")

    def on_button_pressed(self, button):
        i = 0
        for c in self.gamepads:

            if button in c:
                pin = i
                break
            i += 1

        self.log(f'Button {button.name} was pressed.')

        self.send_data(("gamepad", pin, button.name, 1))

    def on_axis_moved_raw(self, axis):
        i = 0
        for c in self.gamepads:
            if axis in c:
                pin = i
                break

        value = axis.value
        self.log(f"Axis {axis.name} moved to {value}")

        self.send_data(("gamepad", pin, axis.name, round(value, 2)))
