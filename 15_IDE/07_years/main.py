a = int(input('Введите первый год:'))
b = int(input('Введите второй год:'))
while a < b:
   for i in range(10):
        if 3 == str(a).count(str(i)):
            print(a)
        a += 1