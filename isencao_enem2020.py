situacao_ensino_medio = input()
fez_encceja = input()
nota_encceja = float(input())
tipo_escola = input()
renda = float(input())
recebeu_isencao = input()
if recebeu_isencao == 's':
    justificou = input()


if situacao_ensino_medio == 'CSC' or situacao_ensino_medio == 'NCC':
    print("Infelizmente voce nao tem direito a isencao")
elif situacao_ensino_medio == 'CVC' or situacao_ensino_medio == 'CLD':

    if nota_encceja >= 400:
        if recebeu_isencao == 'n':
            print("Voce terah direito a isencao")
        else:
            if justificou == 's':
                print("Voce terah direito a isencao")
            else:
                print("Infelizmente voce nao tem direito a isencao")
    else:
        if situacao_ensino_medio == 'CVC':
            if tipo_escola == 'PUB':
                if recebeu_isencao == 'n':
                    print("Voce terah direito a isencao")
                else:
                    if justificou == 's':
                        print("Voce terah direito a isencao")
                    else:
                        print("Infelizmente voce nao tem direito a isencao")
            else:
                print("Infelizmente voce nao tem direito a isencao")
        elif situacao_ensino_medio == 'CLD':
            if tipo_escola == 'PUB' or tipo_escola == 'PCB' or tipo_escola == 'PPB':
                if renda <= 1431:
                    if recebeu_isencao == 'n':
                        print("Voce terah direito a isencao")
                    else:
                        if justificou == 's':
                            print("Voce terah direito a isencao")
                        else:
                            print("Infelizmente voce nao tem direito a isencao")
                else:
                    print("Infelizmente voce nao tem direito a isencao")
            else:
                print("Infelizmente voce nao tem direito a isencao")
else:
    print("Informacao sobre ensino medio invalida")
