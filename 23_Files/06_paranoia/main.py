def ceasar_encode(letter, shift):
    result = ''
    for letter in line:
        if letter.isalpha():
            number = ord(letter) + shift % 32
            if number > 1103:
                number -= 32
            result += chr(number)
        else:
            result += letter
    return result


text = open('text.txt', encoding='utf-8').read().splitlines()
ave_text = [text for text in text if text]
for shift, line in enumerate(ave_text, 1):
    print(ceasar_encode(line, shift), '\n')