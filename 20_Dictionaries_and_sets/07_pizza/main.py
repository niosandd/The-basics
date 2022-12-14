def fun(dct, key, arg):
    dct[key] = dct.setdefault(key, 0) + int(arg)
    return dct


d = {}
for _ in range(int(input('Введите кол-во заказов: '))):
    _, fio, pizza, amount = input().rsplit(maxsplit=3)
    d[fio] = fun(d.get(fio, {}), pizza, amount)

for name in sorted(d):
    print(f'{name}:')
    for pizza, amount in sorted(d.get(name).items()):
        print(f'{pizza}: {amount}')
    print()