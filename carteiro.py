[n,m] = map(int,input().split(" "))
casas = list(map(int,input().split(" ")))
encomendas = list(map(int,input().split(" ")))

i = 0
c = 0
n = -1
x = 1
for k in encomendas:
    if n > k:
        x = -1
    else:
        x = 1
    while casas[c] != k:
        i += 1
        c += x
        if casas[c] == k:
            n = k
            break
print(i)