def calculaArea(largura, comprimento):
    return largura * comprimento

#Programa principal
a = float(input("Digite o Largura: "))
b = float(input("Digite o Comprimento: "))

print("Area: {}".format(calculaArea(a,b)))