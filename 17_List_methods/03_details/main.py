shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
name = input('Название детали: ')
count = 0
price_sum = 0
for product in shop:
    if product[0] == name:
        count += product.count(name)
        price = product[1]
        price_sum += price
print(f'\nКол-во деталей - { count } \nОбщая стоимость - { price_sum } ')