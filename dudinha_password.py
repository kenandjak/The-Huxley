N = int(input())
trechos = []
for i in range(N):
    D = input()
    S = input()
    if D == 'd':
        trechos.append(S[:6])
    elif D == 'e':
        p = S[6:]
        tam = len(p)
        palavra_invertida = ''
        while tam > 0:
            palavra_invertida += p[tam-1]
            tam -= 1
        trechos.append(palavra_invertida)
P = input()

p_circular = ''
for palavra in trechos:
    p_circular += palavra

p_circular = p_circular + trechos[0]

tam_2 = len(p_circular)
p_circular_invertida = ''
while tam_2 > 0:
    p_circular_invertida += p_circular[tam_2 - 2]
    tam_2 -= 1

p_circular += p_circular_invertida

cont = 0
y = 0
x = 0
length = len(p_circular)
while x < length:
    if p_circular[x] == P[y]:
        x += 1
        y += 1
        if y > (len(P) - 1):
            cont += 1
            y = 0
    else:
        if y != 0:
            y = 0
        else:
            x += 1

senha = (P+str(cont))

print(senha)