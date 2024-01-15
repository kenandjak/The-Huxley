# Selection Sort
def ordenacao(v):
    tam = len(v)
    for i in range(tam):
        menor = i
        for j in range(i+1,tam):
            if v[j] < v[menor]:
                menor = j
        v[i],v[menor] = v[menor],v[i]
    return v

n = int(input())
k = list(map(int,input().split(" ")))

vetor = ordenacao(k)

# Formato de saída
for y in range(len(vetor)):
    print(vetor[y], end=' ')
print()