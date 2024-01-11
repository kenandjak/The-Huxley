[d,p,u,n] = map(int,input().split(" "))

a = abs(d - p)
b = abs(a - u)

total = d + a + b + n

print(total)