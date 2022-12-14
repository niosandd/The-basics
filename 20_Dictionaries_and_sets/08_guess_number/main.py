n = int(input('Введите максимальное число: '))
a = set(range(1, n+1))
for x in iter(lambda: input('Нужное число есть среди вот этих чисел: '), 'Помогите!'):
    b = set(map(int, x.split()))
    if input('Ответ Артёма: ') == 'Да':
        a &= b
    else:
        a -= b
print(*a)