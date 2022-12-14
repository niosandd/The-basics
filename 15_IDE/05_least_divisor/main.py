def divider(N):
    for k in range(2, int(N ** 0.5 + 1)):
        if N % k == 0: return k
    return N

print('Наименьший делитель, отличный от единицы:', divider( int(input()) ) )
