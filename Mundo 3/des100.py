"""FACA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NUMEROS E DUAS FUNCOES CHA,MADAS SORTEIA() E SOMA PAR(). A PRIMEORA FUNCAO VAI SORTEAR 5 NUMEROS E VAI COLOCAR - LS DENTRO DA LIOSTA E A SEGUNDA FUNCAO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNCAO ANTERIORES."""

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n}', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')



numeros = list()
sorteia(numeros)
somaPar(numeros)
