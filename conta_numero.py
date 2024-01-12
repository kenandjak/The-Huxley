y = int(input())
total = 0
cont = 0
d = 0
for i in range(20):
    n = int(input())
    if n == -1:
        break
    elif n > 0 and n < 15 or n > 20:
        total += n
        d += 1
        if n == y:
            cont += 1
    else:
        if n == y:
            cont += 1

print("O número",y,"apareceu",cont,"vez(es)")
if total == 0:
    print("Sem valores para calcular a média")
else:
    media = total / d
    media = '%.2f' % float(media)
    print("A média dos números foi de:",media)
