# -*- coding: utf-8 -*-

def errorclose(reason, platform):
    if platform == None:
        print(f'The program encountered a problem and needs to close.\nError: “{reason}”')
    if platform == 'windows':
        from win10toast import ToastNotifier as toast # Solutions must be found to reduce the size of the dependencies (win32 especially).

        toast().show_toast('Fatal error !', f'PiDeck driver has stopped.\nError: “{reason}”', "C:\\Firmin\\PiDeck\\logo\\PiDeck_logo.ico", 5, True) # Show notification if PiDeck needs to close because of an important error.
    else:
        print(f'The program encountered a problem and needs to close.\nError: “{reason}”')

try:
    import change_volume as vol
    import prog_init as init
    from os import system as systex

    platform = init.check_platorm() # Run the function to test if the platform on which the program is run is supported.
    if platform == 'windows':
        systex('python wsgi_waitress.py') # Run the HTTP server.
        print('win')
    elif platform == 'macos':
        systex("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi_gunicorn:app") # Run the HTTPS server.
    elif platform == 'linux':
        pc_init = init.init_lnx() # Run the function to initialize the program.
        systex("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi_gunicorn:app") # Run the HTTPS server.

except:
    try:
        platform
    except NameError:
        platform = None
    errorclose(reason="Unknown", platform=platform)