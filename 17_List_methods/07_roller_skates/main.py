shoes_size = []
feet_size = []
suitable_list = []

N = int(input("Кол-во коньков: "))
for number in range(N):
    print("Размер ", number + 1, " пары: ", end="")
    size = int(input())
    shoes_size.append(size)

K = int(input("Кол-во людей: "))
for number in range(K):
    print("Размер ноги ", number + 1, " человека: ", end="")
    size = int(input())
    feet_size.append(size)

for index_shoes in range(N):
    for index_feet in range(K):
        if shoes_size[index_shoes] == feet_size[index_feet]:
            suitable_list.append(feet_size[index_feet])

unique_list = list(set(suitable_list))
print("Наибольшее кол-во людей, которые могут взять ролики: ", len(unique_list))