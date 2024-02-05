[a,b,c] = map(int,input().split(" "))
if a+b>c and b+c>a and c+a>b:
    if a == b and a == c:
        print("eh equilatero")
    elif a != b and a != c and b != c:
        print("eh escaleno")
    else:
        print("eh isosceles")
else:
    print("nao eh triangulo")