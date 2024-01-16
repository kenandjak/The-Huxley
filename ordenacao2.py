# Insertion Sort
def ordenacao(v):
    for i in range(1,len(v)):
        key = v[i]
        j = i - 1
        while j >= 0 and key < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key
    return v

n = int(input())
k = list(map(int,input().split(" ")))

vetor = ordenacao(k)

# Formato de saída
for y in range(len(vetor)):
    print(vetor[y], end=' ')
print()