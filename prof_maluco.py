def recursivo(n=input()):
    if n == '0':
        return ''
    else:
        return recursivo(n=input()) + '\n'+ n
    
print(recursivo())