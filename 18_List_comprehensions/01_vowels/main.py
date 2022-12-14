word = input('Введите текст: ')
vowels = [i for i in word if i in 'уеыаоэяию']
print(vowels)
print('Длина списка:', len(vowels))