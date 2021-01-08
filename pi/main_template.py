# 2021 Adelta
# https://github.com/A-delta

from raspimote.pi import Pi


IP = "Your IP"
pi = Pi(IP, "WiFi")        # Create Pi object (WiFi only for now)

pi.add_config([{"pin": "21", "type_input": "button"}])  # Add a button on GPIO 21

pi.add_USB_Device(1)
"""
Add a USB Device, see https://github.com/A-delta/RaspiMote/blob/main/utility/identify_usb_device.py
to know which number you must write.
"""

pi.establish_connection()  # Create connection and get connection code from Driver on your computer

pi.run()  # Start sending data
