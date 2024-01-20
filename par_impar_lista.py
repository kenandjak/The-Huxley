n = int(input())
par = []
impar = []
for i in range(n):
    text = input()
    inputs = list(map(str, text.split(" ")))
    if (len(inputs) < 2):
        inputs = map(str, text.split("\t"))
    
    [nome, g] = inputs
        
    if int(g) % 2 == 0:
        par.append(nome)
    else:
        impar.append(nome)
print()
for x in par:
    print(x)
for y in impar:
    print(y)

'''
print('ana\t2')'''