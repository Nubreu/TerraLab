lista = []

ler = "s"
while ler == "s":
    lista.append(int(input("Digite um numero: ")))
    ler = input("s - continuar | n - encerrar ")

elementos = len(lista)
lista.sort(reverse=True)
print("\nA lista possui {} elementos".format(elementos))
if 5 in lista:
    print("O valor 5 esta na lista")
else:
    print("O valor 5 não esta na lista")
print(lista)
