qtd_vendas = 0
qtd_vista = 0
forma_vendas = {'C':0,'V':0}
lista_idade = []
maior_compra = []
while True:
    idade = int(input())
    valor = float(input())
    forma = input()
    c = input()
    qtd_vendas += 1
    lista_idade.append(idade)
    maior_compra.append(valor)
    if forma == 'C':
        forma_vendas['C'] += valor
    else:
        qtd_vista += 1
        forma_vendas['V'] += valor
    if c == 'N':
        break
if qtd_vista > 0:
    media = forma_vendas['V'] / qtd_vista
else:
    media = 0
print()
print(qtd_vendas)
print(round(forma_vendas['V'],2))
print(round(forma_vendas['C'],2))
print(min(lista_idade))
print(max(maior_compra))
print(round(media,2))