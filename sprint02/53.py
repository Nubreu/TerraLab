#palindromos
frase = input("Digite uma frase ou palavra: ")
frase = frase.strip()
frase = frase.upper()
fraseAnalise = frase.replace(" ", "")

palindromo = True
tamanho = len(fraseAnalise)
for a in range(0,tamanho):
    if fraseAnalise[a] != fraseAnalise[tamanho-1-a]:
        palindromo = False
        break

if palindromo:
    print("A frase \"{}\" é um palidromo".format(frase))
else:
    print("A frase \"{}\" não é um palidromo".format(frase))