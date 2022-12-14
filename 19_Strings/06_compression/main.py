s = input()
l = len(s)
cnt = 1
for i in range(l):
    if i == (l - 1):
        print(s[i] + str(cnt), end='')
    else:
        if s[i] == s[i + 1]:
            cnt = cnt + 1
        else:
            print(s[i] + str(cnt), end='')
            cnt = 1