N = int(input('Введите число: '))

spisok= []

for i in range(1, N):
    if i % 2:
        spisok.append(i)
print(spisok)