level = int(input())

if level >= 1 and level <= 20:
    p = (level ** 3) + 20
elif level <= 40:
    p = (level - 10)**2 + 8000
elif level <= 60:
    p = level*5 + 9000
elif level <= 80:
    p = level*2 + 9300
elif level <= 100:
    p = level + 9500

print("Potencia de :",p,"W")