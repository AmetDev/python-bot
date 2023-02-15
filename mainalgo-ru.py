import json
import keyboard
import requests

BASE_URL = "http://45.130.43.65:9090/posts"
response = requests.get(BASE_URL)
response_json = response.json()

running = True
free_space = 0

print("Введите уникальный идентификатор и запомните его. При последующем вводе введите его:")
user_id = int(input())

user_found = False
for element in response_json:
    
    if element.get('owner_id') == user_id:
        user_found = True
        break

if not user_found:
    new_element = {"owner_id": user_id}
    new_element["owner_name_parking"] = input("Введите название парковки:")
    new_element["owner_password"] = int(input("Введите PIN-код:"))
    new_element["index_city"] = int(input("Введите почтовый индекс вашего города"))
    new_element["owner_price_parking"] = int(input("Введите стоимость парковки:"))
    new_element["owner_free_forinvalid"] = input("Бесплатно для инвалидов (yes/no):").lower() == "yes"
    new_element["owner_number_parking_spaces"] = int(input("Введите количество свободных мест:"))
    new_element["User_number_of_free_place_parking"] = new_element["owner_number_parking_spaces"]
    new_element["User_number_of_occupied_parking_spaces"] = 0
    response = requests.post(BASE_URL, data=json.dumps(new_element), headers={'Content-Type': 'application/json'})

else:
    for element in response_json:
        if element.get('owner_id') == user_id:
            print('Добро пожаловать!')
            print("Введите свой PIN-код, если Вы уже зарегистрированы")
            password = int(input())
            if element.get("owner_password") == password:
                print('Чтобы обновить количество свободных мест, нажмите пробел')
                print('Чтобы выйти из программы, нажмите N')
                while running == True:
                    if keyboard.is_pressed('space'):
                        print("Изменилось ли количество свободных мест? Указывать:")
                        free_space = int(input())
                        element["User_number_of_free_place_parking"] = free_space
    
                        update_url = BASE_URL + "/" + str(element["owner_id"])
                        response = requests.put(update_url, data=json.dumps(element), headers={'Content-Type': 'application/json'})
                        if response.status_code == 200:
                            print("Обновлено количество бесплатных парковочных мест!")
                        else:
                            print("Не удалось обновить количество бесплатных парковочных мест")

                   
                    if keyboard.is_pressed('n'):
                        running = False
