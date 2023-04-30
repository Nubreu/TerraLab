lista = list()
cadastro = dict()
cadastro['Nome'] = ''
cadastro['Sexo'] = ''
cadastro['Idade'] = ''
ler = 's'
while ler == 's':
    cadastro['Nome'] = input('Digite o nome: ')
    cadastro['Idade'] = int(input('Digite a idade: '))
    cadastro['Sexo'] = input('Digite o sexo: ')
    lista.append(cadastro.copy())
    ler = input('\nCadastrar outra pessoa "s"\nEncerrar "n": ')

soma = 0
qtd = len(lista)
for i in lista:
    soma += i['Idade']

media = soma / qtd
print('~~'*25)
print('Pessoas cadastradas: {}'.format(qtd))
print('Media de idade: {}'.format(media))
#Impressao da lista de mulheres
c = 0
print('Lista de Mulheres')
for i in lista:
    if i['Sexo'] == 'F':
        print(f"    {c+1} - {i['Nome']}, {i['Idade']} anos")
        c += 1
c = 0
print('Idade Acima da Media')
for i in lista:
    if i['Idade'] > media:
        print(f'    {c+1} - {i["Nome"]}, {i["Idade"]} anos')
        c += 1