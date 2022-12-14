guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']



while True:

    print('Сейчас на вечеринке', len(guests), 'человек:', guests)

    answer = input('Гость пришёл или ушёл? ').lower()

    if answer == 'пришёл':

        guest_name = input('Имя гостя: ')

        if len(guests) < 6:

            print('Привет, ' + guest_name + '!')

            guests.append(guest_name)

        else:

            print('Прости, ' + guest_name + ', но мест нет')



    if answer == 'ушёл':

        guest_name = input('Имя гостя: ')

        print('Пока, ' + guest_name + '!')

        if guest_name in guests:

            guests.remove(guest_name)



    if answer == 'пора спать':

        print('Вечеринка закончилась, все легли спать.')

        break