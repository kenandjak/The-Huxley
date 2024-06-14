vetor = []
while(True):
    comando = list(map(str,input().split(" ")))
    if comando[0] == "Finalizar":
        break
    elif comando[0] == "Enfileirar":
        vetor.append(int(comando[1]))
    elif comando[0] == "Desenfileirar":
        del vetor[0]
    else:
        for i in range(len(vetor)):
            if i == len(vetor) - 1:
                print(vetor[i])
            else:
                print(vetor[i],end=' ')