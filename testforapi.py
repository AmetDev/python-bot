import requests

response = requests.put("http://45.130.43.65/items/:id")
print(response.text)

