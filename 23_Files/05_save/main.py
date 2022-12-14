import os

text = str(input(f'Введите строку: \n'))
way = str(input(
    f'Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n'))
filename = str(input(f'Введите имя файла: \n'))

testpath = way.replace(" ", "/")

path = str('C:/' + testpath)

newpath = str(testpath + "/" + filename)
print(newpath)
abs_path = os.path.abspath(filename)
print(abs_path)
check_file = os.path.exists(abs_path)
print(check_file)
if check_file:
    ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
    if ans_q == 'да':
        with open(filename, 'w') as file_object:
            file_object.write(text)
            print(f'Файл успешно перезаписан!')
    else:
        print(f'Data is not record')
else:
    with open(filename, 'w') as file_object:
        file_object.write(text)
        print(f'Файл успешно сохранён!')