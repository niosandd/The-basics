a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

count_1 = 0
count_2 = 0
count_3 = 0

a.extend(b)

for i in a:
    if i == 5:
        count_1 += 1
        a.remove(5)

a.extend(c)
for i in a:
    if i == 3:
        count_2 += 1

print('Кол-во цифр 5 при первом объединении: ', count_1)
print('Кол-во цифр 3 при втором объединении:', count_2)
print('Итоговый список: ', a)
