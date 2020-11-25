import requests
import json

url = 'http://localhost:9876/action'
content = {"code": "0000", "id": "12345", "value": "12345"}
headers = {"Content-Type": "application/json"}
content = json.dumps(content)
x = requests.post(url, data=content, headers=headers)
print(x.content)