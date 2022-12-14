from collections import Counter

inp = 'zen.txt'
letters = 0
words = 0
lines = 0

for line in open(inp):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

rare_letter = Counter(str(letters))
rare_letter = min(rare_letter, key=rare_letter.get)


print(f'Количество букв в файле: {letters}')
print(f'Количество слов в файле: {words}')
print(f'Количество строк в файле: {lines}')
print(f'Наиболее редкая буква: {rare_letter}')