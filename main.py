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

# a = ["He90998988978987878898967698k", "25", "hER"]
# B = []
# for elements in a:
#     index = a.index(elements)
#     if(index == 0):
#         index = 'name'
#     if(index == 1):
#         index = 'street'
#     if(index == 2):
#         index = 'city'
#     elements = index + ":" + elements
#     B.append(elements)
#     # print(elements)
# arr = np.array(B)
# list1 = arr.tolist()
# print(list1)

with open('test.json', 'r') as f:
    templates = json.load(f)
    print("придумайте и введите ваш уникальный id")
    user = int(input())
    for elements in templates:
        print(elements)
    if (elements.get('id') != user):
        print(elements.get('id'))
        elements['id'] = user
    templates.append(elements)
    print(templates)
            
    with open('test.json', 'w') as d1:
        json.dump(templates, d1, indent = 4)