[f,b,m] = map(int,input().split(' '))
[x,y,z] = map(int,input().split(' '))

total = 0
if x - f >= 0:
    total += x - f
if y - b >= 0:
    total += y - b
if z - m >= 0:
    total += z - m

print(total)