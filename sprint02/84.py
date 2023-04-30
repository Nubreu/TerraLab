lista = []
pessoa = []
ler = "s"
maiorPeso = 0
menorPeso = 7000

while ler == "s":
    pessoa.append(input("Digite o nome: "))
    pessoa.append(float(input("Digite o peso: ")))

    if pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1]
    if pessoa[1] < menorPeso:
        menorPeso = pessoa[1]

    lista.append(pessoa[:])
    pessoa.clear()
    ler = input("Continuar \"s\" | encerrar \"n\": ")

print("-_"*20)

print("\nO maior peso foi {:.2f}Kg\n Pessoas com maior peso: ".format(maiorPeso),end="")
for i in lista:
    if i[1] == maiorPeso:
        print("{}, ".format(i[0]),end="")

if len(lista) == 1:
    menorPeso = maiorPeso

print("\n\nO menor peso foi {:.2f}Kg\n Pessoas com menor peso: ".format(menorPeso),end="")

for i in lista:
    if i[1] == menorPeso:
        print("{}, ".format(i[0]),end="")

print("\n\nPessoas Cadastradas: ",len(lista))