from lan_server import app
from waitress import serve

serve(app, host='0.0.0.0', port=9876)