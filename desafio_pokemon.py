def contest(x,y):
    if x == y:
        return 'Empate'
    else:
        if x == 'Planta':
            if y == 'Agua':
                return 'Vantagem'
            else:
                return 'Desvantagem'
        elif x == 'Fogo':
            if y == 'Planta':
                return 'Vantagem'
            else:
                return 'Desvantagem'
        else:
            if y == 'Fogo':
                return 'Vantagem'
            else:
                return 'Desvantagem'

a = input()
d = input()
print(contest(a,d))