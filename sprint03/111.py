from utilidadesCeV import moeda

valor = str(43.7834)

print("Aumento 10%: R${}".format(moeda.aumentar(valor,10)))
print("Reducao 10%: R${}".format(moeda.diminuir(valor,10)))
print("      Dobro: R${}".format(moeda.dobro(valor)))
print("     Metade: R${}".format(moeda.metade(valor).replace('.',',')))