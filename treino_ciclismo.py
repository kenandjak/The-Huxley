desempenho = {'otimo':0}

for i in range(7):
    d = float(input())
    if d >= 8:
        desempenho['otimo'] += 1
if desempenho['otimo'] >= 5:
    print("Desempenho otimo")
elif desempenho['otimo'] >= 3:
    print("Desempenho razoavel")
else:
    print("Desempenho ruim")
    