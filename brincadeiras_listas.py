n = list(map(int,input().split(" ")))

invert = []
a = ''
parimp = []
soma = []

def saida(v):
    s = ''
    for x in range(len(v)):
        v[x] = str(v[x])
        if x == len(v) - 1:
            s += v[x]
            return s
        else:
            s += v[x] + ' '

for i in range(len(n)):
    invert.append(n[(-i-1)])
for j in range(len(n)):
    if j % 2 == 0:
        parimp.append(n[j])
for k in range(len(n)):
    if k % 2 != 0:
        parimp.append(n[k])
for l in range(len(n)):
    soma.append(invert[l]+parimp[l])

print(f"Invert: {saida(invert)}\nParImp: {saida(parimp)}\nSoma: {saida(soma)}")
