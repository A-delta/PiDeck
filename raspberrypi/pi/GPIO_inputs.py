from gpiozero import Button, LED
from threading import Thread

class Mixin:
    def add_ADC_Device_PCF8591(self, number_channels):
        """
        I have no idea of how to support other ADCDevice for the moment.
        :return:
        """
        from ADCDevice import PCF8591
        self.log(f"ADC Device added with {number_channels} channels used")
        self.ADC = PCF8591()
        self.ADC_channels += (number_channels - 1)

        self.ADC_old_values = []
        for channel in range(self.ADC_channels + 1):
            self.ADC_old_values.append(int(self.ADC.analogRead(channel)))

        adc_device_thread = Thread(name="USB Device Reading", target=self.run_ADC)
        adc_device_thread.start()

    def run_ADC(self):
        idle = 0
        time_sleep = 0.15
        while True:
            for channel in range(self.ADC_channels + 1):
                old = self.ADC_old_values[channel]
                new = int(self.ADC.analogRead(channel))

                if old not in [new - 1, new, new + 1]:

                    idle = 1
                    time_sleep = 0.1

                    self.ADC_old_values[channel] = new

                    new = int((new / 255) * 100)

                    if self.verbose:
                        print(f"ADC{channel} : {new}", end='; ')
                    self.send_data(("ADC", channel, "adc_event", new))

                elif idle != 0:
                    idle += 1
                    if idle > 100:
                        self.log("Sleep mode")
                        time_sleep = 0.2
                        idle = 0

    def add_buttons(self, config):
        """
        Add buttons configuration. You should run this methods only once.
        Only buttons type devices can be added with this method.

        :param config: list of dictionaries : [{"pin": "GPIO_PIN, "type_device": "button"}]
        :return:
        """
        for device in config:
            device, pin = self.get_input_device(device)

            self.buttons.append(device)
            self.pins.append(pin)

    def get_input_device(self, device):
        """
        This function is designed to handle multiple devices, there's only one for the moment.
        :param device:
        :return:
        """

        pin = device["pin"]
        type_input = device["type_input"]

        self.log(f"Configuring : GPIO{pin}, {type_input}")

        if type_input == "button":
            new = Button(pin)
            new.when_activated = self.event_button

            return new, pin

        # Here you can add support for a device to make it easier to setup (for json configuration files for example.

        else:
            self.log(self.term_warning + type_input + "in" + pin + "not supported, add your own code for it or verify given information" + self.term_endc)


    def event_button(self, button):
        pin = self.pins[self.buttons.index(button)]
        self.log(f"Button{pin}")
        self.send_data(("button", pin, "button_event", 1))
