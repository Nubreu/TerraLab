import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(opcao,arquivoInexistente = False, erroArquivo = False):
    clear()
    print('-'*40)
    print('\t\t\t\t  MENU')
    print('-'*40)
    if opcao < 1 or opcao > 3:
        print('\t\tVALOR DIGITADO INCORETO!')
    if erroArquivo:
        print('\t\tERRO AO REALIZAR GRAVACAO!')
    if arquivoInexistente:
        print('\t\tARQUIVO INEXISTENTE!')

    print('ESCOLHA UMA OPCAO')
    print(' 1 - LISTAR PESSOAS\n 2 - CADASTRAR PESSOAS\n 3 - SAIR')

def filtro():
    while True:
        entrada = str(input('Digite uma opcao: '))
        if entrada.isnumeric():
            break
    
    return int(entrada)

def menu(arquivoInexistente = False, erroArquivo = False):
    opcao = 1
    while True:
        display(opcao,arquivoInexistente,erroArquivo)
        opcao = filtro()
        if opcao < 4 and opcao > 0:
            return opcao
    

