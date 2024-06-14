vetor = list(map(int, input().split(" ")))
count = {}
size = len(vetor)
for i in range(size):
    if not vetor[i] in count:
        count[vetor[i]] = 1
    else:
        count[vetor[i]] += 1
print("Moda =",max(count, key=count.get))