def QHofstadter(start):
    if start != [1, 1]: return
    seq = start[:]
    while 1:
        q = seq[-seq[-1]] + seq[-seq[-2]]
        seq. append(q)
        yield q
i = 1
for x in QHofstadter([1, 1]):
    if i > 33: break
    print(x, end="")
    i += 1