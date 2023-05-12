import urllib
import urllib.request

def disponivel(url = ''):
  try:
    site = urllib.request.urlopen(url)
  except urllib.error.URLError:
    print(f'\n[{url}] [X] INDISPONIVEL')
  else:
    print(f'\n[{url}] [\u2713] DISPONIVEL')

url = 'http://www.pudim.com.br'
disponivel(url)

url = 'https://www.youtube.com/'
disponivel(url)