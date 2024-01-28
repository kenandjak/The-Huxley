n = int(input())
[a,c,b] = map(str,input().split(" "))
a = int(a)
b = int(b)
if c == '+':
    r = a + b
elif c == '*' or c == 'x':
    r = a * b

if r > n:
    print("OVERFLOW")
else:
    print("OK")