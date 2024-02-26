def periodoHistorico(ano,referencia):
    if referencia == 'ac':
        if ano >= 4000:
            return 'PRE-HISTORIA'
        else:
            return 'ANTIGUIDADE'
    elif referencia == 'dc':
        if ano <= 476:
            return 'ANTIGUIDADE'
        elif ano <= 1453:
            return 'IDADE MEDIA'
        elif ano <= 1789:
            return 'IDADE MODERNA'
        else:
            return 'IDADE CONTEMPORANEA'

ano = int(input())
r = input().lower()
print(periodoHistorico(ano,r))