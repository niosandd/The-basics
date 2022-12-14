N = int(input("Кол-во друзей: "))
K = int(input("Кол-во долговых расписок: "))
friends_list = []

for _ in range(N):
    friends_list.append(0)

for number in range(K):
    print("\n", number + 1, "расписка: ")
    from_who = int(input("От кого: "))
    to_who = int(input("Кому: "))
    how_much = int(input("Сколько: "))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print("Баланс друзей: ")
for index in range(len(friends_list)):
    print(index + 1, ": ", friends_list[index])