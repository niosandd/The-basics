s1 = input('Первая строка: ')
s2 = input('Вторая строка: ')
if s2 == s1:
    print('Строки идентичны')
elif len(s2) != len(s1):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    k = 1
    mozhno = False
    for i in range(len(s2)-1):
        s2 = s2[-1]+s2[:-1]
        if s2 == s1:
            mozhno = True
            print ('Первая строка получается из второй со сдвигом', k)
            break
        else:
            k += 1
    if not mozhno:
        print ("Первую строку нельзя получить из второй с помощью циклического сдвига.")