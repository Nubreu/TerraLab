# .strip remove espacos no inicio e no final da string, mas mantem os do meio
# .rfind reverse find, ultima ocorrencia
# .count conta numero de vezes
frase = """   xVamos verV  """
letra = "V"
frase = frase.strip()
vezes = frase.count(letra)
primeira = frase.find(letra)
ultima = frase.rfind(letra)
print("Numero de vezes: {}\nPrimeira Ocorrencia: {}\nUltima Ocorrencia: {}".format(vezes, primeira, ultima))
