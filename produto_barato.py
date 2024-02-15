p1 = float(input())
p2 = float(input())
p3 = float(input())

produtos = [p1,p2,p3]
i = produtos.index(min(produtos))
if i == 0:
    print('Primeiro produto')
elif i == 1:
    print('Segundo produto')
else:
    print('Terceiro produto')