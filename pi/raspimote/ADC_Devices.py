class Mixin:
    def add_ADC_Device_PCF8591(self, number_channels):
        """
        I have no idea of how to support other ADCDevice for the moment.
        :return:
        """
        from ADCDevice import PCF8591

        self.has_ADC = True
        self.log(f"ADC Device added with {number_channels} channels used")
        self.ADC = PCF8591()
        self.ADC_channels += (number_channels - 1)

        self.ADC_old_values = []
        for channel in range(self.ADC_channels + 1):
            self.ADC_old_values.append(int(self.ADC.analogRead(channel)))

        adc_device_thread = Thread(name="USB Device Reading", target=self.run_ADC)
        adc_device_thread.start()


    def run_ADC(self):
        if not self.has_ADC:
            print("NO ADC")  # need to clean errors
        else:
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

                        self.send_data({"code": self.code, "request": {"type": "ADC", "pin": channel, "value": new}})

                    elif idle != 0:
                        idle += 1
                        if idle > 100:
                            self.log("Sleep mode")
                            time_sleep = 0.2
                            idle = 0
