import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
todos = json.loads(response.text)

for entry in todos:
    if (entry['id'] == 1):
        entry['name'] = 'Java'
    print(entry['name'])

print(json.dumps(todos))