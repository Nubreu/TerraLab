r1 = float(input("Digite o tamanho da reta r1: "))
r2 = float(input("Digite o tamanho da reta r2: "))
r3 = float(input("Digite o tamanho da reta r3: "))
triangulo = False
if (r1 + r2 > r3) and (r3 + r2 > r1) and (r1 + r3 > r2):
    triangulo = True

if triangulo:
    if r1 == r2 == r3:
        print("Triangulo Equilatero")
    elif r1 != r2 and r1 != r3 and r3 != r2:
        print("Triangulo Escaleno")
    else:
        print("Triangulo Isoceles")
else:
    print("As retas não formam um triangulo")