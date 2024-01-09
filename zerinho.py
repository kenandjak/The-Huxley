z = list(map(int,input().split(" ")))
if sum(z) == 3 or sum(z) == 0:
    print('*')
else:
    if sum(z) == 1:
        i = z.index(max(z))
        z[0],z[1],z[2] = 'A','B','C'
        print(z[i])
    elif sum(z) == 2:
        i = z.index(min(z))
        z[0],z[1],z[2] = 'A','B','C'
        print(z[i])