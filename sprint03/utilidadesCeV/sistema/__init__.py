def cadastrar():
    nome = ''
    idade = 0
    while True:
        print('Digite o nome: ',end='')
        nome = str(input())
        if nome == '':
            return False
        break
    while True:
        print('Digite a idade: ', end='')
        idadeStr = str(input())
        if idadeStr == '':
            return False
        if idadeStr.isnumeric():
            idade = int(idadeStr)
            break
    return [nome,idade]

def criarArquivoTxt(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        return False
    else:
        return True

def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        return False
    else:
        for linha in arq:
            dado = linha.split(';')
            print(f'Nome: {dado[0]} \nIdade: {dado[1]}',end='')
            print("--"*20)
    arq.close()
    
def buscarArquivo(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def escrever(arqNome,nome = 'N/A', idade = -1):
    try:
        arq = open(arqNome,'at')
    except:
        return False
    else:
        arq.write(f'{nome};{idade}\n')
        arq.close()
        return True

def gravarArquivo(arqNome, lista):
    if buscarArquivo(arqNome):
        return not escrever(arqNome,lista[0],lista[1])
    else:
        criarArquivoTxt(arqNome)
        return not escrever(arqNome, lista[0], lista[1])
