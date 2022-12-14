with open('numbers.txt') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None)[:])))
