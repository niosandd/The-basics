def capitalize(line):
    return ' '.join([s.capitalize() for s in line.split()])
text = input('Введите строку: ')
print('Результат: ',capitalize(text))