result = [ ]
with open('calc.txt', 'r') as file:
    for line in file.readlines():
        try:
            result.append(eval(line))
        except:
            if input('Обнаружена ошибка:' + line + 'Хотите исправить?') == 'да':
                line = input('Введите исправленную строку:')
                result.append(eval(line))
print(sum(result))