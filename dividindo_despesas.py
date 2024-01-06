p = {'Clara':0,'Diana':0}
total = 0
for i in range(6):
    valor_conta = float(input())
    nome = input()
    p[nome] += valor_conta
    total += valor_conta

if p['Clara'] > total/2:
    d = p['Clara'] - total/2
    d = "%.2f" % float(d)
    print("DIANA")
    print(d)
elif p['Diana'] > total/2:
    c = p['Diana'] - total/2
    c = "%.2f" % float(c)
    print("CLARA")
    print(c)
else:
    print("MORADORAS QUITES")