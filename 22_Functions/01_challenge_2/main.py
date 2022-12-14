def num_sequence(num,i = 1):
    print(i, end=" ")
    if i != num:
        num_sequence(num,i+1)

num_sequence(5)