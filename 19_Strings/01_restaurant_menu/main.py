menu = input('Список людей через точку запятую: ')
words_in_menu = menu.split()
menu_one = ';'.join(words_in_menu)
menu_second = ','.join(words_in_menu)
print('Доступное меню:', menu_one)
print('На данный момент в меню есть:', menu_second)