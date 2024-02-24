def resto(dividendo,divisor):
    if divisor == 0:
        return -1
    elif dividendo < 0:
        if divisor < 0:
            if dividendo > divisor:
                return dividendo
            else:
                return resto(dividendo-divisor,divisor)
        else:
            if dividendo >= 0:
                return dividendo
            else:
                return resto(dividendo-divisor,divisor)
    else:
        if divisor < 0:
            if dividendo < -divisor:
                return dividendo
            else:
                return resto(dividendo-divisor,divisor)
        else:
            if dividendo < divisor:
                return dividendo
            else:
                return resto(dividendo-divisor,divisor)

a = int(input())
b = int(input())

print(resto(a,b))