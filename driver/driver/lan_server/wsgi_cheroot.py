from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher as WSGIPathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter
from sys import argv

from lan_server import app


if "-verbose" in argv or "-v" in argv:
     verbose = True
else:
     verbose = False

my_app = WSGIPathInfoDispatcher({'/': app}, verbose=verbose)
server = WSGIServer(('0.0.0.0', 9876), my_app, verbose=verbose)

ssl_cert = "cert.pem"
ssl_key = "key.key"
server.ssl_adapter =  BuiltinSSLAdapter(ssl_cert, ssl_key, verbose=verbose)

if __name__ == '__main__':
     try:
         server.start(verbose=verbose)
     except KeyboardInterrupt:
         server.stop()