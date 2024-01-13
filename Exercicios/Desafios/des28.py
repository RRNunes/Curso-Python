# Escreva um programa que faca o computador 'pensar'em um numero inteiro entre 0 e 5 e peca para o usuario. tentar dsscobrir qual foi o numero escolhido pelo computador
# o programa devera escrecer na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número de 0 a 5 tente adivinhar...')
jogador = int(input('Em que numero pensei?'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Voce acertou o numero!')
else:
    print('Voce perdeu!!!!O numero que pensei foi {} e nao {}. '.format(computador, jogador))

    