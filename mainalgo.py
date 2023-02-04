import keyboard

a = True
free_space = int()

print('Здравствуйте! \n Чтобы обновить данные количества свободных мест нажмите пробел \n Чтобы выйти из программы нажмите Н')

while a == True:
	if keyboard.is_pressed('space'):
		print("кол-во свободных мест изменилось? укажите")
		free_space= input(int())
		print(free_space)
	if keyboard.is_pressed('y'):
		a = False


