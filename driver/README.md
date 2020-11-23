# PiDeck ─ driver  
This driver allows you to control your PiDeck and to personalize the actions of the buttons.


## Dependencies
The driver rests on a few open source modules or programs :
* On every platform :
    * [Flask](https://github.com/pallets/flask), to build the LAN server;
    * [Gunicorn](https://github.com/benoitc/gunicorn) to serve it.
* On Linux:
    * [xdotool](https://github.com/jordansissel/xdotool), to control the keyboard (simulate a volume button press for instance);
    * [ALSA utils](https://github.com/alsa-project/alsa-utils), to retreive the current sound volume.
* On macOS:
    * [mac-volume](https://github.com/andrewp-as-is/mac-volume), to control the sound volume.