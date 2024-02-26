"""FACA UM PROGRAMA QUE TENHA UMA FUNCAO CHA,MADA maior(), QUE RECEBA VARIOS PARAMETROS COM VALORES INTEIROS. SEU PROGRAMA TEM QUE ANALIZAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.
"""
from time import sleep
def maior(*num):
    cont = maior = 0
    print('\nAnaliozando os valores passados...')
    for valor in num:
        print(f' {valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
