from gpiozero import Button, LED
from time import sleep, time
from signal import pause
import threading

class Pi:
    def __init__(self, config):
        self.setup(config)

    def setup(self, user_supported_devices):  # user_supported_devices could be a json file

        self.disp_info = True  # NEED TO ADD CHOICE
        self.error_led = LED(18)
        self.success_led = LED(23)

        self.ADCchannels = 0

        self.devices = []
        for device in user_supported_devices:
            self.devices.append(self.get_input_device(device))


    def get_input_device(self, device):
        """
        This function is designed to handle multiple devices, there's only one for the moment.
        :param device:
        :return:
        """


        pin = device["pin"]
        type_input = device["type_input"]

        print(f"Configuring : GPIO{pin}, {type_input}")

        if type_input == "button":
            new = Button(pin)
            new.when_activated = self.event_button

            return new

        # Here you can add support for a device to make it easier to setup (for json configuration files for example.

        else:
            print(type_input, "in", pin, "not supported, add your own code for it or verify given information")


    def add_ADC_Device(self, number_channels):
        """
        I have no idea of how to support other ADCDevice for the moment.
        :return:
        """
        from ADCDevice import PCF8591
        self.ADC = PCF8591()
        self.ADCchannels += (number_channels-1)

        self.ADC_old_values = []
        for channel in range(self.ADCchannels + 1):
            self.ADC_old_values.append(int((self.ADC.analogRead(channel)/255)*100))


    def run(self):
        adc = False
        try:
            if self.ADC != None:
                print("got a ADC device")
                adc = True
        except:
            pass

        if adc:
            idle = 0
            time_sleep = 0.15
            while True:

                for channel in range(self.ADCchannels+1):
                    old = self.ADC_old_values[channel]
                    new = int((self.ADC.analogRead(channel)/255)*100)

                    if old != new:

                        idle = 1
                        time_sleep = 0.075

                        self.ADC_old_values[channel] = new
                        self.send_data({"TYPE": "ADC", "pin": channel, "value": new})

                    elif idle != 0:
                        idle += 1
                        if idle > 100:
                            print("Sleep mode")
                            time_sleep = 0.2
                            idle = 0
        else:
            pause()

    def show_success(self):
        self.success_led.on()
        sleep(0.1)
        self.success_led.off()
        sleep(0.1)
        self.success_led.on()
        sleep(0.1)
        self.success_led.off()

    def show_error(self):
        self.error_led.on()
        sleep(0.1)
        self.error_led.off()
        sleep(0.1)
        self.error_led.on()
        sleep(0.1)
        self.error_led.off()



    def event_button(self, button):
        print(button.pin)
        self.send_data({"TYPE": "button", "pin": button.pin, "value": 1})

    def send_data(self, data):
        print(data["value"])
        success = True
        if success:
            t = threading.Thread(name='Blink LED', target=self.show_success)
        else:
            t = threading.Thread(name='Blink LED', target=self.show_error)

        t.start()
        return


