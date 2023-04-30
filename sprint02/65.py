ler = "s"
menorPossivel = -5
maior = 0
menor = -1
soma = 0
leituras = 0
while ler == "s":
    num = int(input("Digite um numero para ler "))
    if num > maior:
        maior = num
    if menor > num > menorPossivel:
        menor = num
    soma += num
    leituras += 1
    ler = input("Digite \"s\" para ler e \"n\" para parar ")

media = soma/leituras
print(" Maior lido: {}".format(maior))
if menor != -1:
    print(" Menor lido: {}".format(menor))
else:
    print(" Menor lido: {}".format(maior))
print(" Media: {:.2f}".format(media))