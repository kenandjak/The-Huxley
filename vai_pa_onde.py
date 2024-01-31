cidades = {}
while True:
    nome = input()
    if nome.lower() != 'fim':
        km = int(input())
        valor = float(input())
        gasto = valor * 2
        if gasto <= 300:
            cidades[nome] = km
            cidade = nome
    else:
        break
if len(cidades) == 0:
    print('SEM DESTINO')
else:
    maior = cidades[cidade]
    name = cidade
    for cidade in cidades:
        if cidades[cidade] > maior:
            maior = cidades[cidade]
            name = cidade
    print(name.upper())

