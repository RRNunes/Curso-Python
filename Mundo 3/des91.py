"""WXERCICIO 091: JOGO DE DADOS EM PYTHON

CRIE UM PROGRAMA ONDE 4 JOGADORES JOGEM UMDADO E TENHAM RESULTADOS ALEATORIOS. GUARDE ESSES RESULTADOS EM UM DICIONARIO. NO FINAL, COLOQUE ESSE DICIONARIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NUMERO DO DADO.
"""

from random import randint
from time import sleep
from operator import intemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=intemgetter(1), reverse=True)
print('-=' * 30)
print(f' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'  {i + 1}o lugar: {v[0]} com {v[1]}. ')
    sleep

    