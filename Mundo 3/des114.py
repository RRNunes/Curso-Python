"""
Exercício Python 114:
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://wwww.pudim.com.br')
except:
    print('ERRO! O site pudim nao esta acessivel no momento.')
else:
    print('OK! Consegui acessar o site pudim.')
    print(site.read())



