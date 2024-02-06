[x,y,q] = map(int,input().split(" "))
a = 0
if True:
    if x > 0 and y > 0:
        if q == 2:
            a = y+1
            b = x+1
            i = 'y'
            j = 'x'
        elif q == 4:
            b = y+1
            a = x+1
            i = 'x'
            j = 'y'
        else:
            print("caminhada invalida\n")
    elif x < 0 and y > 0:
        x = -x
        if q == 1:
            b = x+1
            a = y+1
            i = 'y'
            j = 'x'
        elif q == 3:
            a = x+1
            b = y+1
            i = 'x'
            j = 'y'
        else:
            print("caminhada invalida\n")
    elif x < 0 and y < 0:
        x = -x
        y = -y
        if q == 2:
            a = x+1
            b = y+1
            i = 'x'
            j = 'y'
        elif q == 4:
            b = x+1
            a = y+1
            i = 'y'
            j = 'x'
        else:
            print("caminhada invalida\n")
    elif x > 0 and y < 0:
        y = -y
        a = x+1
        b = y+1
        if q == 1:
            a = x+1
            b = y+1
            i = 'x'
            j = 'y'
        elif q == 3:
            b = x+1
            a = y+1
            i = 'y'
            j = 'x'
        else:
            print("caminhada invalida\n")
    if a != 0:
        print(f"{a} passos em {i} e {b} passos em {j}")