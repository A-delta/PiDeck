from cheroot.wsgi import Server as WSGIServer
from cheroot.wsgi import PathInfoDispatcher as WSGIPathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter

from lan_server import app

my_app = WSGIPathInfoDispatcher({'/': app})
server = WSGIServer(('0.0.0.0', 9876), my_app)

ssl_cert = "cert.pem"
ssl_key = "key.key"
server.ssl_adapter =  BuiltinSSLAdapter(ssl_cert, ssl_key, None)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()