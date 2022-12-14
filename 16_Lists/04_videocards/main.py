video_card = int(input('Введите количество видеокарт: '))
new_spisok = []
old_spisok = []

for vc in range(0, video_card):
    question = int(input('Видеокарта: '))
    old_spisok.append(question)

new_spisok.append(old_spisok)

max_n_in_new_spisok = max(new_spisok)
print('Наибольшее:', max_n_in_new_spisok)
a = new_spisok.remove(max_n_in_new_spisok)

print(a)

