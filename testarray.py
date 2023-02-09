import json
import keyboard
import requests

BASE_URL = "http://localhost:5000/posts"
response = requests.get(BASE_URL)
response = response.json()

a = True
free_space = int()

print("Введите уникальный идентификатор и запомните его. При последующим входе введете его:")
user = int(input())

user_found = False
for elements in response:
    
    if elements.get('owner_id') == user:
        user_found = True
        break

if not user_found:
    new_element = {"owner_id": user}
    new_element["owner_name_parking"] = input("Введите название парковки:")
    new_element["owner_password"] = int(input("Введите пин-код:"))
    new_element["owner_price_parking"] = int(input("Введите цену парковки:"))
    new_element["owner_free_forinvalid"] = input("Бесплатно для льготников (yes/no):").lower() == "yes"
    new_element["owner_number_parking_spaces"] = int(input("Введите количество свободных мест:"))
    new_element["User_number_of_free_place_parking"] = new_element["owner_number_parking_spaces"]
    new_element["User_number_of_occupied_parking_spaces"] = 0
    response = requests.post(BASE_URL, json = new_element)

else:
    for elements in response:
        if elements.get('owner_id') == user:
            print('Добро пожаловать!')
            print("Введите ваш пин-код, если уже зарегистрированы!")
            password = int(input())
            if elements.get("owner_password") == password:
                print('Чтобы обновить количество свободных мест, нажмите пробел')
                print('Для выхода из программы нажмите N')
                while a == True:
                    if keyboard.is_pressed('space'):
                        print("Количество свободных мест изменилось? Указать:")
                        free_space = int(input())
                        elements["owner_number_parking_spaces"] = free_space
                        elements["User_number_of_free_place_parking"] = free_space
                        print("Обновлено количество бесплатных парковочных мест!")
                    if keyboard.is_pressed('n'):
                        a = False
    

