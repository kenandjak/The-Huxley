[n,m] = map(int,input().split(" "))
casas = list(map(int,input().split(" ")))
encomendas = list(map(int,input().split(" ")))

i = 0
c = 0
n = -1
x = 1
for k in encomendas:
    if n > k:
        x = -1
    else:
        x = 1
    while casas[c] != k:
        i += 1
        c += x
        if casas[c] == k:
            n = k
            break
print(i)

'''if __name__ == '__main__':
    st_line = [int(x) for x in input().strip().split(' ')]
    nd_line = [int(x) for x in input().strip().split(' ')]
    rd_line = [int(x) for x in input().strip().split(' ')]

    houses = st_line[0]
    letters = st_line[-1]

    moves = 0

    last_house = 0
    for house in rd_line:
        in_houses = nd_line.index(house)
        if last_house > in_houses:
            moves += last_house - in_houses
        elif last_house < in_houses:
            moves += in_houses - last_house
        last_house = in_houses

    print(moves)'''