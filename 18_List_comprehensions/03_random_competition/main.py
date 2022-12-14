from random import uniform

first = list(round(uniform(5, 10), 2) for i in range(20))
second = list(round(uniform(5, 10), 2) for i in range(20))
winners = list()
for i in range(len(first)):
    if first[i] > second[i]:
        winners.append(first[i])
    else:
        winners.append(second[i])

print("Первая команда: ", first)
print("Вторая команда: ", second)
print("Победители: ", winners)