[a,b,c] = map(int,input().split(" "))

vencedor = max(a,b,c)
terceiro = min(a,b,c)
meio = a + b + c - vencedor - terceiro

if vencedor != terceiro and vencedor != meio:
    if vencedor == a:
        print(f"O vencedor é Introducao a Programacao com um total de {a} votos E O HEXA VEIO.")
    elif vencedor == b:
        print(f"O vencedor é Introducao a Computacao com um total de {b} votos.")
    else:
        print(f"O vencedor é Calculo 6 com um total de {c} votos.")
else:
    print("Empate.")