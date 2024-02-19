""""FACA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES.O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS  SERAO GERADOS E VAI SORTEAR 6 NUMEROS ENTRE 1 E 60 PARA CADA JOGO.CADASTRADOS TUDO EM UMA LISTA COMPOSTA.
"""

from random import randint
from time import sleep
lista =  list()
jogos = list()
print('-' * 30)
print('      JOGO NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quabtos jogos voce quer que eu sorteie? '))
tot  = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO... {quant} JOGOS ','-=' * 30)
for i, l in enumerate(jogos):
    print(f'Jogos {i + 1}: {1}')
    sleep(1)
print('-=' * 5, 'BOA SORTE! > ', '-=' * 5)
