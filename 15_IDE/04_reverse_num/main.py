def reversed(number):
    flag = True
    whole = ''
    fraction = ''
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole = whole + symbol
        else:
            fraction = fraction + symbol
    reverse = float(fraction + '.' + whole)
    return reverse

number1 = (input('Введите первое число: '))
number2 = (input('Введите второе число: '))

result1 = reversed(number1)
result2 = reversed(number2)
total = result1 + result2
print('Первое число: ', result1, '\nВторое число: ', result2, '\n Сумма равна: ', total)

