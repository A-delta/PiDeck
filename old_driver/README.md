# RaspiMote ─ driver  
This driver controls your RaspiMote, following your configuration.


## Dependencies
The driver rests on a few open source modules or programs:
* On every platform :
    * [Flask](https://github.com/pallets/flask), to build the LAN server.
* On Linux:
    * [xdotool](https://github.com/jordansissel/xdotool), to control the keyboard (simulate a volume button press for instance).
    * [ALSA utils](https://github.com/alsa-project/alsa-utils), to retreive the current sound volume.
    * [Gunicorn](https://github.com/benoitc/gunicorn), to serve the LAN server with the HTTPS protocol.
* On macOS:
    * [mac-volume](https://github.com/andrewp-as-is/mac-volume), to control the sound volume.
    * [Gunicorn](https://github.com/benoitc/gunicorn), to serve the LAN server with the HTTPS protocol.
* On Windows:
    * [NirCmd](https://github.com/gillstrom/nircmd), to control the sound volume.
    * [Waitress](https://github.com/Pylons/waitress), to serve the LAN server with the HTTP protocol.