import requests
import json

url = 'https://localhost:9876/connect'
content = {"code": "0000"}
headers = {"Content-Type": "application/json"}
content = json.dumps(content)
x = requests.request('CONNECT', url, data=content, headers=headers, verify=False)
print(x.content)