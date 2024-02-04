n = int(input())
if n % 3 == 0:
    i = 2
    cont = 1
    while 3 * i <= n:
        if n % (3 * i) == 0:
            cont += 1
        i += 1
    print('Digite um numero inteiro:')
    print('Quantidade de divisores divisiveis por 3:',cont)
else:
    print('Digite um numero inteiro:')
    print('O numero nao possui divisores multiplos de 3')