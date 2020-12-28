# -*- coding: utf-8 -*-

def errorclose(reason, platform):
    if platform == None:
        print(f'The program encountered a problem and needs to close.\nError: “{reason}”')
        exit()
    if platform == 'windows' or platform == 'macos' or platform == 'linux': # Show notification if RaspiMote needs to close because of an important error.
        from tkinter import Tk, messagebox
        window = Tk()
        window.withdraw()
        messagebox.showerror('RaspiMote ─ error', f'The program encountered a problem and needs to close\nError: “{reason}”')
        exit()
    else:
        print(f'The program encountered a problem and needs to close.\nError: “{reason}”')
        exit()


import prog_init as init
from os import system as systex

platform = init.check_platorm() # Run the function to test if the platform on which the program is run is supported.
if platform == 'windows':
    print('Enter Pi IP adress :')
    ip = input()
    connect = init.connect(ip, platform)
    if connect == True:
        print('Success! Connection established!')
    else:
        errorclose("Connection failed", platform)

    systex('python wsgi_waitress.py') # Run the HTTP server.
elif platform == 'macos':
    errorclose(reason="macOS is not supported for now.", platform=platform)
    """
    THIS PART OF THE PROGRAM IS DISABLED AS MANY THINGS DON'T WORK ON macOS.

    systex("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi_gunicorn:app") # Run the HTTPS server.
    """
elif platform == 'linux':
    #print('Enter Pi IP adress :')
    ip = "192.168.1.37"
    #ip = input()
    connect = init.connect(ip, platform)
    print(connect)
    if connect == True:
        print('Success! Connection established!')
    else:
        errorclose("Connection failed", platform)

    pc_init = init.init_lnx() # Run the function to initialize the program.
    systex("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi_gunicorn:app") # Run the HTTPS server.
