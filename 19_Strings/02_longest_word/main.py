text = input('Самое длинное слово: ')
text = text.replace('.', '').replace(',', '').replace(':', '').replace('!', '').replace('?', '').split()
print(', '.join([word for word in text if len(word) == len(sorted(text, key=len)[-1])]).lower())