valor = float(input())
categoria = input()

if categoria.upper() == 'N':
    preco = '%.2f' % float(valor)
    print(f"Preco sem desconto: R${preco}")
elif categoria.upper() == 'E':
    preco = valor/2
    preco = '%.2f' % float(preco)
    print(f"Preco com desconto: R${preco}\nCategoria: Estudante")
elif categoria.upper() == 'A':
    preco = valor * 0.7
    preco = '%.2f' % float(preco)
    print(f"Preco com desconto: R${preco}\nCategoria: Aposentado")
else:
    print("Categoria invalida!")