lista = list()
for i in range(0,5):
    lista.append(int(input(f"Digite o {i+1}° Numero ")))
maiorValor = lista[0]
menorValor = lista[0]
maiorIndex = 0
menorIndex = 0
for c,i in enumerate(lista):
    if i >= maiorValor:
        maiorIndex = c
        maiorValor = i
    if i < menorValor:
        menorIndex = c
        menorValor = i
print(lista)
print("Maior valor {} | index {}".format(maiorValor,maiorIndex))
print("Menor valor {} | index {}".format(menorValor,menorIndex))