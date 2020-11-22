# -*- coding: utf-8 -*-

def errorclose(reason):
    print(f'The program encountered a problem and needs to close.\nError : “{reason}”')

try:
    import change_volume as vol
    import prog_init as init
    from os import system as systex

    if init.check_platorm() == 'linux':
        pc_init = init.init_lnx()
        systex("gunicorn --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:9876 wsgi:app")

except:
    errorclose(reason="Unknown")