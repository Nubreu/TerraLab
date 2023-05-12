def maior(lista):
    listaOrdenada = sorted(lista)
    return listaOrdenada[len(lista)-1]

#Programa Pricipal
lista = list()

ler = 's'
while ler == 's':
    lista.append(int(input("Digite um numero: ")))
    ler = input('Para continuar lendo digite "s": ')

print("Maior elemento: {}".format(maior(lista)))