goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item in goods:
    item_name = item
    item_code = goods[item]
    item_quantity, item_total_amount = 0, 0

    for i in store[item_code]:
        item_quantity += i['quantity']
        item_total_amount += i['price'] * i['quantity']


    print(item_name, item_quantity, 'шт, стоимость', item_total_amount, 'руб')
