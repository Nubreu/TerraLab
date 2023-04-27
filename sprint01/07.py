#Media Aritmetica
nota1 = nota2 = nota3 = -1.0
while(nota1 > 10 or nota1 < 0):
    nota1 = float(input("Digite a nota 1 do aluno: "))
while(nota2 > 10 or nota2 < 0):
    nota2 = float(input("Digite a nota 2 do aluno: "))
while(nota3 > 10 or nota3 < 0):
    nota3 = float(input("Digite a nota 3 do aluno: "))
media = (nota1+nota2+nota3)/3
print("A media aritmetica do aluno é {:.2f}".format(media))