#Numero Primo
primo = True
num = int(input("Digite um numero inteiro: "))

for a in range(2,num):
    if num % a == 0:
        primo = False
        break
if primo:
    print("O numero {} é primo".format(num))
else:
    print("O numero {} não é primo".format(num))
