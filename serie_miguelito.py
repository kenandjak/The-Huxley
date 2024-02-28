def serieMiguelito(index,i=1,n=3):
    if i == index:
        return n
    else:
        if i % 2 == 0:
            return serieMiguelito(index,i+1,n+1)
        else:
            return serieMiguelito(index,i+1,n+4)

index = int(input())
print(serieMiguelito(index))
