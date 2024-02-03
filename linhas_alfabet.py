alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
while True:
    c = input()
    if c == 'F':
        break
    else:
        local = alfabeto.find(c)
        seq = alfabeto[:local+1]
        seq += ' '
        print(seq)