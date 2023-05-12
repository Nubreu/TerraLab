def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('Voce não digitou um inteiro')


print("Numero: {}".format(leiaInt('Digite um inteiro: ')))