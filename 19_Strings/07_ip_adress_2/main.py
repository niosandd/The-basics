ip = input()
split_ip = ip.split('.')
if len(split_ip)<4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    numeric = 0
    out_of_range = 0
    for x in split_ip:
        if x.isdigit():
            numeric+=1
            if int(x)>255:
                out_of_range+=1
                print(x,'превышает 255')
            else:
                print(x,'- не целое число')
    if out_of_range==0 and numeric == 4:
        print('IP-адрес корректен')