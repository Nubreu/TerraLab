#Tratamento de Erros e Exceções
x = 0
# Alguns tipos de erro de exceção
# x = 2/0
# x = 2/'2'
# lst= [3,6,4]
# print(lst[3])

try:
    # operacao
    a = int(input('A: '))
    b = int(input('B: '))
    r = a / b
    print(f'Resultado: {r}')
except:
    # falhou
    print('Falhou')
finally:
    print('Vai ser executado de qualquer maneira')