frase = input()
frase = frase.lower()
vogais = {'a':0,'e':0,'i':0,'o':0,'u':0}
v = 0
total = 0
for letra in frase:
    total += 1
    if letra in vogais:
        v += 1
        vogais[letra] += 1
pctg = '%.2f'%float(v*100/total)
print(f"a {vogais['a']}\ne {vogais['e']}\ni {vogais['i']}\no {vogais['o']}\nu {vogais['u']}\n{pctg}%")
