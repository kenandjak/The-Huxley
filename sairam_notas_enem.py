def busca(x,v):
    inicio = 0
    fim = len(v)-1
    while inicio <= fim:
        ind = (inicio + fim)//2 
        meio = v[ind]
        if x == meio:
            return ind
        else:
            if x < meio:
                fim = ind - 1
            else:
                inicio = ind + 1
    return False

cpfs = []
notas = []
ps = []
n = int(input())
for i in range(n):
    cpf = int(input())
    cpfs.append(cpf)
for j in range(n):
    nota = int(input())
    notas.append(nota)
m = int(input())
for k in range(m):
    p = int(input())
    ps.append(p)

for a in ps:
    resultado = busca(a,cpfs)
    if resultado == False:
        print('NAO SE APRESENTOU')
    else:
        print(notas[resultado])
