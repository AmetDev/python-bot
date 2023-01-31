import requests
import json
import numpy as np
import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# todos = json.loads(response.text)
#
# for entry in todos:
#     if (entry['id'] == 1):
#         entry['name'] = 'Java'
#     print(entry['name'])
#
# print(json.dumps(todos))

a = ["Hek", "25", "hER"]
B = []
for elements in a:
    index = a.index(elements)
    if(index == 0):
        index = 'name'
    if(index == 1):
        index = 'street'
    if(index == 2):
        index = 'city'
    elements = f"'{index}': {elements}"
    B.append(elements)
    # print(elements)
arr = np.array(B)
list1 = arr.tolist()
with open('test.json', 'w') as f:
    json.dump(list1, f)
#



