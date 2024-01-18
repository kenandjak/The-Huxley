alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def busca(l,alfabeto):
    inicio = 0
    final = len(alfabeto) - 1
    while inicio <= final:
        x = (inicio + final)//2
        meio = alfabeto[x]
        if l == meio:
            return x
        elif l < meio:
            final = x - 1
        else:
            inicio = x + 1

string = input()
frase = ''
for letra in string:
    if letra == ' ':
        frase += ' '
    else:
        indice = busca(letra,alfabeto)
        letra = alfabeto[-(indice+1)]
        frase += letra
print(frase)