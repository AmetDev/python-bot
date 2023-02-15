import json
import keyboard
import requests

BASE_URL = "http://45.130.43.65:9090/posts"
response = requests.get(BASE_URL)
response_json = response.json()

running = True
free_space = 0

print("Enter a unique identifier and remember it. On subsequent entry, enter it:")
user_id = int(input())

user_found = False
for element in response_json:
    
    if element.get('owner_id') == user_id:
        user_found = True
        break

if not user_found:
    new_element = {"owner_id": user_id}
    new_element["owner_name_parking"] = input("Enter the name of the parking lot:")
    new_element["owner_password"] = int(input("Enter the PIN code:"))
    new_element["index_city"] = int(input("Введите почтовый индекс вашего города"))
    new_element["owner_price_parking"] = int(input("Enter the price of parking:"))
    new_element["owner_free_forinvalid"] = input("Free for the handicapped (yes/no):").lower() == "yes"
    new_element["owner_number_parking_spaces"] = int(input("Enter the number of free spaces:"))
    new_element["User_number_of_free_place_parking"] = new_element["owner_number_parking_spaces"]
    new_element["User_number_of_occupied_parking_spaces"] = 0
    response = requests.post(BASE_URL, data=json.dumps(new_element), headers={'Content-Type': 'application/json'})

else:
    for element in response_json:
        if element.get('owner_id') == user_id:
            print('Welcome!')
            print("Enter your PIN code if already registered!")
            password = int(input())
            if element.get("owner_password") == password:
                print('To update the number of free spaces, press space')
                print('To exit the program, press N')
                while running == True:
                    if keyboard.is_pressed('space'):
                        print("Has the number of free spaces changed? Indicate:")
                        free_space = int(input())
                        element["User_number_of_free_place_parking"] = free_space
    
                        update_url = BASE_URL + "/" + str(element["owner_id"])
                        response = requests.put(update_url, data=json.dumps(element), headers={'Content-Type': 'application/json'})
                        if response.status_code == 200:
                            print("The number of free parking spaces has been updated!")
                        else:
                            print("Failed to update the number of free parking spaces")

                   
                    if keyboard.is_pressed('n'):
                        running = False
