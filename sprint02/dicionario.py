# {} -> simboliza um dicionario
# criacao de um dicionario
##dados = dict()

dados = {'nome': 'Pedro', 'idade': 23, 'Sexo': 'M'}

#Criando novo elemento dados['Sexo'] = 'M'

#Removendo elementos
del dados['idade']
#===================================================
filme = dict()
filme['titulo'] = 'Star Wars'
filme['ano'] = 1997
filme['diretor'] = 'George Lucas'
#Imprime elementos
print(filme.values())
#Imprime os "tipos"
print(filme.keys())
#Imprime ambos
print(filme.items())
#=======================================================
print("")
print("=="*20)

for k, v in filme.items():
    print("O {} é {}".format(k,v))

#=======================================================
print("")
print("=="*20)
## O metodo copy serve para conseguir adicionar o dicionário na lista
locadora = list()
locadora.append(filme.copy())

filme["titulo"] = 'Avengers'
filme['ano'] = '2012'
filme['diretor'] = 'Joss Whedon'
locadora.append(filme.copy())

filme["titulo"] = 'Matrix'
filme['ano'] = '1999'
filme['diretor'] = 'Wachowski'
locadora.append(filme.copy())

print(locadora)
#percorre liste
for i in locadora:
    print('~~' * 20)
    #imprime dicionario
    for j, k in i.items():
        print("{}: {} ".format(j.upper(),k))