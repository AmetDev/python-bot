import requests
url = "http://localhost:5000/posts"

params = {'index_city': 95000}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(data)
    # process the returned data
else:
    # handle error
     print("Request failed with status code:", response.status_code)
