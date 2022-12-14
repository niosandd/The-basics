count = int(input('Введите количество пар слов: '))
text_dict = dict()
for i_count in range(1, count + 1):
    text = input(f'{i_count}пара: ').lower().split(' - ')
    text_dict[text[0]] = text[1]
    text_dict[text[1]] = text[0]
while True:
    word = input('\введите слово: ').lower()
    if word in text_dict:
        print('Синоним:', text_dict[word])
    else:
        print('Такого слова в словаре нет.')