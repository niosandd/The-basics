word = input('Введите слово: ')
syms_list = []
for i_sym in word:
    count_char = 0
    for y_sym in word:
        if i_sym == y_sym:
            count_char += 1
        if count_char > 1:
            break
    if count_char == 1:
        syms_list.append(i_sym)
print('Кол-во уникальных букв:', len(syms_list))
print('Сами буквы:', *syms_list)