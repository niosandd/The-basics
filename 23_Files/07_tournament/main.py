new_file = open("first_tour.txt", "r", encoding="utf8")
k = int(new_file.readline())

new_list = []

for line in new_file:
    new_line = line.split()

    if new_line != [] and int(new_line[-1]) > k:
        new_list.append(new_line)
new_file.close()

new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()

count = str(len(new_list))

out_lst = []
n = 1
for i in new_list:
    name_sim = str(i[0][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i[1] + ' ' + i[-1]
    out_lst.append(s_win)
    n += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    s = '\n'.join(out_lst)
    f_out.write(s)

for i in out_lst:
    print(f'{i}')