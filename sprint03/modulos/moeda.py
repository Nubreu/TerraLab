def aumentar(valor, aumento):
    if isinstance(valor,float):
        return valor * (1 + aumento/100)
    else:
        valorFloat = float(valor) * (1 + aumento/100)
        valorStr = '{:.2f}'.format(valorFloat)
        return '{}'.format(valorStr).replace('.', ',')

def diminuir(valor, reducao):
    if isinstance(valor,float):
        return valor * (1 - reducao/100)
    else:
        valorFloat = float(valor) * (1 - reducao/100)
        valorStr = '{:.2f}'.format(valorFloat)
        return '{}'.format(valorStr).replace('.', ',')
def dobro(valor):
    if isinstance(valor,float):
        return valor * 2
    else:
        dobroFloat = float(valor) * 2
        dobroStr = '{:.2f}'.format(dobroFloat)
        return '{}'.format(dobroStr).replace('.', ',')
def metade(valor):
    if isinstance(valor,float):
        return valor / 2
    else:
        metadeFloat = float(valor) / 2
        metadeStr = '{:.2f}'.format(metadeFloat)
        return '{}'.format(metadeStr).replace('.', ',')

def resumo(valor,aumento,reducao):
    print('Valor Analisado: R${}\n'.format(valor))
    print('        Dobro : R${}'.format(dobro(valor)))
    print('        Metade: R${}'.format(metade(valor)))
    print(f'{aumento}% de aumento: R${aumentar(valor,aumento)}')
    print(f'{reducao}% de reducao: R${diminuir(valor,reducao)}')