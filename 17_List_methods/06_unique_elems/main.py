from collections import OrderedDict
a = [1, 2, 3]
b = [2, 4, 6, 3, 3, 2, 1]
c = []

print('Первый список равен: ', a)
print('Второй список равен: ', b)

c.extend(a)
c.extend(b)

d = list(OrderedDict.fromkeys(c))

print(d)
