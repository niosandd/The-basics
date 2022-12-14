file = input('Введите имя файла: ')
if not file.endswith('.txt', '.docx'):
    print('Ошибка: неверное расширение файла')
if file.startswith(' @№$%^&*()'):
    print('Ошибка:недопустимый символ')
else:
    print('Файл назван верно')

