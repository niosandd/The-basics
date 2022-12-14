import random

errors = [ArithmeticError, AssertionError, AttributeError]
r, f = 0, open('nums.txt', 'w')

with f as file:
    while r <= 777:
        n = int(input())
        r += n
        if random.choices((0, 1), (1-1/13, 1/13))[0]:
            raise random.choice(errors)
        print(n, file=file)