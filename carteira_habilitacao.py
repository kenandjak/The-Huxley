idade = int(input())

d = idade - 18

if d >= 0:
    print(f"\nVoce ja pode tirar habilitacao!\nVoce tem direito a habilitacao ha {d} ano(s)")
else:
    d = 18 - idade
    print(f"\nVoce precisa esperar mais {d} ano(s)!")