valor1 = float(input("Digite o primeiro valor "))
valor2 = float(input("Digite o segundo valor "))
valor3 = float(input("Digite o terceiro valor "))

if valor1 > valor2 and valor1 > valor3:
    print("O valor {} é o maior".format(valor1))
elif valor2 > valor1 and valor2 > valor3:
    print("O valor {} é o maior".format(valor2))
else:
    print("O valor {} é o maior".format(valor3))
exit()
