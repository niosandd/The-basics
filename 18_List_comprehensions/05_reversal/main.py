n = input('')
firsth = n.index('h')
secondh = n.rindex('h')
print(n[:firsth+1]+n[secondh-1:firsth:-1]+n[secondh:])