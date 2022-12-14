def sum_of_digits(n):
    return sum(map(int, str(abs(n))))


def count_of_digits(n):
    return len(str(abs(n)))


n = int(input('Введите число: '))
s, c = sum_of_digits(n), count_of_digits(n)

print('Сумма равна: ', s, '\nРазность равна: ', s - c)