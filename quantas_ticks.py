[d,c] = map(int,input().split(' '))

minutos = 90 * d
ticks = (1200 * minutos)/c

print(int(ticks))