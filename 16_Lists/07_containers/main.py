i = 0
l = []
k = 0
number = int(input('Количество контейнеров: '))
for _ in range(number):
    l.append(int(input('Введите вес контейнеров: ')))
k = int(input('\nВведите вес нового контейнера: '))
while i < len(l) and l[i] >= k:
    i += 1
print('\nНомера, куда встанет контейнер:', i + 1)