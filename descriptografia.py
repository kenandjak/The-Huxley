def descrypt(senha,index):
    if index == len(senha):
        return ''
    elif senha[index] == '*':
        index += 1
        return '('+ str(index)+descrypt(senha,index)+')'
    else:
        index += 1
        return str(index) + descrypt(senha,index)

senha = input()
index = 0
print(descrypt(senha,index))