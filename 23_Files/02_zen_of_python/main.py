with open('../03_zen_of_python_2/zen.txt') as f:
    for text in reversed(f.readlines()):
        print(text, end='')
