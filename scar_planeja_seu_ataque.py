d1 = int(input())
d2 = int(input())
m  = int(input())

f = (10 * m) / (d1 + d2)

if f >= 4:
    t = "Eu matei Mufasa"
elif f > 2:
    t = "Consegui lacaios preciosos"
else:
    t = "Mais um fracasso..."

f = "%.2f" % float(f)

print(f"Scar conseguiu criar uma frustração {f} na turma\n{t}")