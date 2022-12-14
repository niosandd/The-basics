def fib(n, c=0, p=1):
    if (n == 0):
        return c
    else:
        return fib(n - 1, c + p, c)


def fibg():
    c, p = 0, 1
    while (True):
        q = c + p
        yield q
        p = c
        c = q


fib_gen = fibg()

for i in range(1, 31):
    print(i, next(fib_gen))