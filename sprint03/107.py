from modulos import moeda

valor = float(input("Digite um numero: "))

print("Aumento 10%: {:.2f}".format(moeda.aumentar(valor,10)))
print("Reducao 10%: {:.2f}".format(moeda.diminuir(valor,10)))
print("      Dobro: {:.2f}".format(moeda.dobro(valor)))
print("     Metade: {:.2f}".format(moeda.metade(valor)))