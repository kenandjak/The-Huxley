# Bubble Sort
def ordenacao(v):
    n = len(v)
    for i in range(n):
        for j in range(0,n-i-1):
            if v[j] > v[j+1]:
                v[j],v[j+1] = v[j+1],v[j]
    return v

n = int(input())
k = list(map(int,input().split(" ")))

vetor = ordenacao(k)

# Formato de saída
for y in range(len(vetor)):
    print(vetor[y], end=' ')
print()