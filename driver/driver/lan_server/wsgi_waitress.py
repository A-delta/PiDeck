# 2021 Adelta
# https://github.com/A-delta


from lan_server import app
from waitress import serve

"""
Entrypoint to run the web server with Waitress.
"""

serve(app, host='0.0.0.0', port=9876)