"""Crie um programa que tenha a funcao leialnt(), que vai funcionar de forma semelhante a funcao input() do python
so que fazendo a validacao para aceitar apenas um valor numerico.
ex: 
n = leialnt('Digite um n')"""


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')
