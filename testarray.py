import json
import keyboard

a = True
free_space = int()

with open('test.json', 'r') as f:
    arr = json.load(f)

print("Введите уникальный идентификатор:")
user = int(input())

user_found = False
for elements in arr:
    if elements.get('id') == user:
        user_found = True
        break

if not user_found:
    new_element = {"id": user}
    new_element["nameparkovka"] = input("Введите название парковки:")
    new_element["password"] = input("Введите пароль:")
    new_element["priceparkovka"] = int(input("Введите цену парковки:"))
    new_element["free_forinvalid"] = input("Бесплатно для льготников (yes/no):").lower() == "yes"
    new_element["number of free parking spaces"] = input("Введите количество свободных мест:")
    arr.append(new_element)
else:
    for elements in arr:
        if elements.get('id') == user:
            print('Добро пожаловать!')
            print('Чтобы обновить количество свободных мест, нажмите пробел')
            print('Для выхода из программы нажмите N')

            while a == True:
                if keyboard.is_pressed('space'):
                    print("Количество свободных мест изменилось? Указать:")
                    free_space = int(input())
                    elements["number of free parking spaces"] = free_space
                    print("Обновлено количество бесплатных парковочных мест!")
                if keyboard.is_pressed('n'):
                    a = False

with open('test.json', 'w') as f:
    json.dump(arr, f, indent=4)
