result = dict()
print('Текущие контакты на телефоне: \n<Пусто>')

while True:
    name = input('Введите имя: ')
    cont = int(input('Введите номер телефона: '))
    if name not in result:
        result[name] = cont
        print('Текущие контакты на телефоне: \n')
    for i in result:
        print(i, result[i])
    else:
        print('Ошибка: такое имя уже существует.')
    break