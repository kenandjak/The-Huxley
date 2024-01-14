pessoas = int(input())
lugar = input()
quartos = int(input())

custo = 0

lugar = lugar.lower()
if lugar == 'pipa':
    custo += 75 * pessoas
    if quartos == 2:
        custo += 600
    elif quartos == 3:
        custo += 900
elif lugar == 'fortaleza':
    custo += 60 * pessoas
    if quartos == 3:
        custo += 950
    elif quartos == 4:
        custo += 1120
quantia = custo / pessoas

print(f"{custo:.2f}")
print(f"{quantia:.2f}")