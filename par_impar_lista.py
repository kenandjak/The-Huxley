n = int(input())
par = []
impar = []
for i in range(n):
    [nome,g] = map(str,input().split(" "))
    if int(g) % 2 == 0:
        par.append(nome)
    else:
        impar.append(nome)
print()
for x in par:
    print(x)
for y in impar:
    print(y)

'''
n = int(input())
par = []
impar = []
for i in range(n):
    nomes = list(map(str,input().split(" ")))
    if int(nomes[-1]) % 2 == 0:
        nome = ''
        for m in range(len(nomes)-1):
            nome += nomes[m]
        par.append(nome)
    else:
        nome = ''
        for m in range(len(nomes)-1):
            nome += nomes[m]
        impar.append(nome)
print()
for x in par:
    print(x)
for y in impar:
    print(y)
'''


'''
print('ana\t2')'''