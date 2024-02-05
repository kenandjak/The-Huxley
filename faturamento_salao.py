pm = {'corte':40,'penteado':50,'maquiagem':70}
sh = {'barba':0,'corte':0}
brb = 0
crt = 0
total = 0
while True:
    c = input()
    c = c.lower()
    if c != 'm' and c != 'f':
        break
    else:
        s = input()
        s = s.lower()
        if c == 'm':
            sh[s] += 1
            ph = {'barba':15,'corte':25}
            total += ph[s]
        elif c == 'f':
            total += pm[s]
total = '%.2f'%float(total)
servico = 'BARBA'
if sh['corte'] > sh['barba']:
    servico = 'CORTE'
elif sh['corte'] == sh['barba'] or sh['barba'] == 0:
    servico = 'AMBOS'
print(servico)
print(total)
