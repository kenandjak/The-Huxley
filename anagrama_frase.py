string1 = input()
string2 = input()

string11 = string1.lower().replace(' ','').replace('.','')
string12 = string11.replace(',','').replace('!','').replace('?','')

string21 = string2.lower().replace(' ','').replace('.','')
string22 = string21.replace(',','').replace('!','').replace('?','')

d1 = {}
for i in string12:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1

d2 = {}
for j in string22:
    if j not in d2:
        d2[j] = 1
    else:
        d2[j] += 1

print(d1 == d2)