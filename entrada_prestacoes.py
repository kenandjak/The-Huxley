valor = float(input())

if valor % 3 == 0:
    prestacao = valor / 3
    prestacao = '%.2f'%float(prestacao)
    print(prestacao)
    print(prestacao)
    print(prestacao)
else:
    prestacoes = 2 * (valor // 3)
    prestacao = valor - prestacoes
    p1 = '%.2f'%float(prestacao)
    p2 = '%.2f'%float(prestacoes/2)
    print(p1)
    print(p2)
    print(p2)

