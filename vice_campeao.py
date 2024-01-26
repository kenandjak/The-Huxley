[a,b,c] = map(int,input().split(" "))
lista = [a,b,c]

maior = lista.index(max(lista))
menor = lista.index(min(lista))

for i in range(3):
    if i != maior and i != menor:
        vice = lista[i]
print(vice)