def add_symb(v):
    j = ''
    for i in range(len(v)):
        v[i] = str(v[i])
        if i == len(v) - 1:
            j += v[i]
            return j
        else:
            j += v[i] + ' ' + '|' + ' '

def insertion_sort(v):
    for i in range(1,len(v)):
        c = v[:]
        j = i - 1
        chave = v[i]
        print("Chave:",chave) 
        print("Estado Atual:",add_symb(c)) 
        while j >= 0 and chave < v[j]:
            v[j+1] = v[j]
            v[j] = chave
            j -= 1
            c = v[:]
            print(add_symb(c))
        #v[j+1] = chave
        print()
    print('Resultado Final:',add_symb(c))

vetor = list(map(int,input().split(" ")))
insertion_sort(vetor)