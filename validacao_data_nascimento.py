def conversor(string):
    inteiro = string
    inteiro = int(string)
    return inteiro

dia = input()
dia = conversor(dia)
if dia >= 1 and dia <= 31:
    mes = input()
    mes = conversor(mes)
    if dia > 29 and mes == 2:
        print("Esse dia não existe nesse mês")
    elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        print("Esse dia não existe nesse mês")
    elif mes < 1 or mes > 12:
        print("Mês inexistente")
    else:
        ano = int(input())
        if ano <= 2020 and ano >= 1900:
            if mes == 2 and dia == 29:
                if ano % 4 == 0:
                    if ano % 100 != 0:
                        print("Data Validada")
                    else:
                        if ano % 400 == 0:
                            print("Data Validada")
                        else:
                            print("Esse ano não é bissexto")
                else:
                    print("Esse ano não é bissexto")
            else:
                print("Data Validada")
        else:
            print("Ano inexistente")
else:
    print("Dia inexistente")
