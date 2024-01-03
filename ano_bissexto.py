n = int(input())

if n % 4 != 0:
    print("NAOBISSEXTO")
else:
    if n % 100 != 0:
        print("BISSEXTO")
    else:
        if n % 400 != 0:
            print("NAOBISSEXTO")
        else:
            print("BISSEXTO")