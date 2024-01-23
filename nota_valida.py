nota = float(input())
n = nota
nota = '%.1f'%float(nota)
print("Nota digitada:",nota)
if n < 0 or n > 10:
    print("A nota nao esta no intervalo [0,10]")
