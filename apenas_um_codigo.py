def funcao(x):
    if x == 2:
        return 'primo'
    elif x % 2 == 0:
        return 'par'
    elif x % 2 != 0:
        if x == 1:
            return 'impar'
        else:
            y = x-2
            while y > 1:
                if x % y == 0:
                    return 'impar'
                else:
                    y -= 2
            return 'primo'

n = int(input())
pontos = {'sapo':0,'shuas':0}
for i in range(n):
    [a,b] = map(int,input().split(" "))
    if funcao(a) == 'par' and funcao(b) == 'impar':
        pontos['sapo'] += 1
    elif funcao(a) == 'par' and funcao(b) == 'primo':
        pontos['shuas'] += 1
    elif funcao(a) == 'impar' and funcao(b) == 'par':
        pontos['shuas'] += 1
    elif funcao(a) == 'impar' and funcao(b) == 'primo':
        pontos['sapo'] += 1
    elif funcao(a) == funcao(b):
        pass
    elif funcao(a) == 'primo' and funcao(b) == 'par':
        pontos['sapo'] += 1
    else:
        pontos['shuas'] += 1
    
if pontos['sapo']>pontos['shuas']:
    print()
    print("Sapo sopa esta de boa na lagoa!")
elif pontos['sapo']<pontos['shuas']:
    print()
    print("Testemunhe a verdadeira forca!")
else:
    print()
    print("Impending doom approaches...")