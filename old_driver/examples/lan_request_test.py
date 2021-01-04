import requests
import json

z = 0
print('Is your server run by :\n1: Gunicorn\n2: Waitress')
y = input('> ')
if y == 1:
    url = 'https://localhost:9876/action'
    z = 1
if y == 2:
    url = 'http://localhost:9876/action'
    z = 1
if z == 1:
    content = {"code": "0000", "id": "12345", "value": "12345"}
    headers = {"Content-Type": "application/json"}
    content = json.dumps(content)
    x = requests.post(url, data=content, headers=headers, verify=False)
    print(x.content)
else:
    print('ERROR')