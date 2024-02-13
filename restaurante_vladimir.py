def precos(produto,sabor):
    if produto == 'pizza':
        if sabor == 'calabresa' or sabor == 'marguerita':
            preco = 20.6
        else:
            preco = 30.9
    elif produto == 'lasanha':
        if sabor == 'queijo':
            preco = 18
        elif sabor == 'bolonhesa':
            preco = 23
    return preco

produto = input().lower()
sabor = input().lower()
qtdd = int(input())

valor = (precos(produto,sabor)+2) * qtdd
print('%.2f'%float(valor))