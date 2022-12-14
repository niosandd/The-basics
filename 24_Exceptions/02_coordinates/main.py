import random

result = list()


def func1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def func2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt') as f:
    data = f.readlines()

for line in data:
    line = line.split()

    try:
        num1, num2 = map(int, line)
    except:
        print('Некорректный данные в файле "coordinates.txt"')
        break

    res1 = func1(num1, num2)
    res2 = func2(num1, num2)
    number = random.randint(0, 100)

    my_list = sorted([res1, res2, number])
    my_list = list(map(str, my_list))

    result.append(' '.join(my_list) + '\n')

with open('result.txt', 'w') as f:
    f.writelines(result)