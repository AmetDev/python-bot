import json

with open('test.json', 'r') as f:
    arr = json.load(f)

print("Enter your unique id:")
user = int(input())

user_found = False
for elements in arr:
    if elements.get('id') == user:
        user_found = True
        break

if not user_found:
    new_element = {"id": user}
    new_element["nameparkovka"] = input("Enter the name of the parking lot:")
    new_element["password"] = input("Enter the password:")
    new_element["priceparkovka"] = int(input("Enter the price of the parking lot:"))
    new_element["free_forinvalid"] = input("Is it free for invalid (yes/no):").lower() == "yes"
    arr.append(new_element)

with open('test.json', 'w') as f:
    json.dump(arr, f, indent=4)
