sym_sum = 0
line_count = 0
with open('people.txt', 'r') as people_file:
    try:
        for i_line in people_file:
            try:
                length = len(i_line)
                line_count += 1
                if i_line.endswith('\n'):
                    length -= 1
                sym_sum += length
                if length < 3:
                    raise ValueError
            except ValueError:
                print('Имя в строке {} меньше трех букв'.format(line_count))
                with open('errors.log', 'a') as error_file:
                    error_file.write(i_line)
    except FileNotFoundError:
        print('Файл не найден ')
    finally:
        print('Сумма символов: ', sym_sum)