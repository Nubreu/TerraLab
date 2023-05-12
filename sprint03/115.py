### A LIMPEZA DO TERMINAL NAO FUNCIONA MUITO BEM NO PYCHARM
from utilidadesCeV import menu
from utilidadesCeV import sistema
arqNome = 'arquivo.txt'
erroArquivo = False
ArquivoInexitente = False

while True:
  opcao = menu.menu(ArquivoInexitente,erroArquivo)
  lixo = ''
  ArquivoInexitente = False
  erroArquivo = False
  if opcao == 1:
      #LISTAR PESSOAS
      menu.clear()
      print('--'*20)
      print('\t\tLISTAGEM DE PESSOAS')
      print('--'*20)
      if sistema.buscarArquivo(arqNome):
          sistema.lerArquivo(arqNome)
          lixo = str(input('\n\tPRESSIONE QUALQUER TECLA'))
      else:
          ArquivoInexitente = True

  elif opcao == 2:
      #CADASTRAR NOVA PESSOA
      menu.clear()
      print('--'*20)
      print('\t\tCADASTRO DE PESSOAS')
      print('--'*20)
      var = sistema.cadastrar()
      if var != False:
          erroArquivo = sistema.gravarArquivo(arqNome,var)
      else:
          erroArquivo = True
  else:
    break