def funcao(x):
    x = "%.2f"%float(x)
    return x

v = float(input())

a = v * 0.9
b = round(v / 3,2)
c = 0.05 * a
d = 0.05 * v

print("A vista com desconto de 10%:",funcao(a))
print("Valor da parcela em 3x sem juros:",funcao(b))
print("Comissao do vendedor a vista:",funcao(c))
print("Comissao do vendedor a prazo:", funcao(d))