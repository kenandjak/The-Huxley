def senhaCalculai(n,d,c,i):
    cont = 0
    senha = ''
    while cont < 5:
        if cont == 4:
            senha += n[cont]+i
        else:
            senha += n[cont]+d[cont]+c[cont]
        cont += 1
    return senha
dados = []

x = 0
while x < 5:
    nome = input()
    if nome == 'SAIR':
        break
    else:
        data = input()
        date = data[:5].replace('/','')
        cidade = input()
        idade = input()
        senha = senhaCalculai(nome,date,cidade,idade)
        dados.append(
            {"Nome: ":nome,
            "Data de Nascimento: ":data,
            "Cidade Natal: ":cidade,
            "Idade: ":idade,
            "Senha: ":senha}
        )
    x += 1

for pessoa in dados:     
    print("Nome:",pessoa["Nome: "])
    print("Data de Nascimento:",pessoa["Data de Nascimento: "])
    print("Cidade Natal:",pessoa["Cidade Natal: "])
    print("Idade:",pessoa["Idade: "],"anos")
    print("Senha:",pessoa["Senha: "])