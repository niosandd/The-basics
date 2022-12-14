def calculation():
    for x in list_1:
        for y in list_2:
            yield x, y
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
start = calculation()
for elem in start:
    print(elem[0], elem[1], elem[0] * elem[1])
    if (elem[0] * elem[1]) == 56:
        print('found!')
        break
