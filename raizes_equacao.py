def calculaDelta(a,b,c):
    if a == 0 or c == 0:
        return 'Impossivel calcular'
    else:
        delta = b**2 - (4 * a * c)
        if delta < 0:
            return 'Impossivel calcular'
        else:
            resultado = calculaRaizes(a,b,delta)
            return resultado

def calculaRaizes(a,b,delta):
    if delta == 0:
        x = -b/(2*a)
        return f'X = {"%.5f"%float(x)}'
    else:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        return f'X1 = {"%.5f"%float(x1)}\nX2 = {"%.5f"%float(x2)}'

[a,b,c] = map(float,input().split(" "))
print('Digite os coeficientes da equacao:')
print(calculaDelta(a,b,c))
