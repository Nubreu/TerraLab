unidade = dezena = centena = milhar = valor = 0.0
valor = int(input("Digite um valor: "))
milhar = valor // 1000 % 10
centena = valor // 100 % 10
dezena = valor // 10 % 10
unidade = valor // 1 % 10

print("M-{:.0f}\nC-{:.0f}\nD-{:.0f}\nU-{:.0f}".format(milhar,centena,dezena,unidade))