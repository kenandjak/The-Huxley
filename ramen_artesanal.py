a = input()
b = input()
c = input()
d = input()
x = -1
if a == 'Carne':
    if b == 'Bamboo':
        if d == 'Ovo':
            if c == 'Sal':
                x = 1
                print("Naruto - ¥500")
            elif c == 'Shoyu':
                x = 1
                print("Luffy - ¥475")
            elif c == 'Nori':
                x = 1
                print("Kirito - ¥450")
    elif b == 'Cebolinha':
        if d == 'Nori':
            if c == 'Kimushi':
                x = 1
                print("Misty - ¥600")
if x == -1:
    print("Está tentando inventar um novo prato? O chef aqui sou eu!")
