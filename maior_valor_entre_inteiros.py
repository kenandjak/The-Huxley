n = int(input())
l = []
maior = 0
posicao = 0
for i in range(n):
    x = int(input())
    l.append(x)
    if l[i] > maior:
        maior = l[i]
        posicao = i
print()
print(f"o maior numero eh {maior}, e foi lido na posicao {posicao}")