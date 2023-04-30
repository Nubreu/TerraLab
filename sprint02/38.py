a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a == b:
    print("Os valores são iguais")
elif a > b:
    print("{} > {}".format(a,b))
else:
    print("{} > {} ".format(b,a))

exit()