#Reajuste Salarial
salario = float(input("Digite o valor do salario do funcionário :"))

salarioFinal = 0.0
reajuste = 15
aumento = ((salario * reajuste)/100.0)
salarioFinal = aumento + salario
print("Salario: R${}\nSalario com reajuste de {}%: R${}\nValor do Reajuste: R${}".format(salario,reajuste,salarioFinal,aumento))