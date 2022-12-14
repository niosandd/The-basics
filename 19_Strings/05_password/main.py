a = input("Введите пароль: ")
total = 0
    if len(a) >= 8:
        for i in a:
            if i in "0123456789":
                total += 1
            if i.upper() in a:
                total += 1

if total >= 4:
    print("Пароль надежный")
else:
        print("пароль ненадежный ")