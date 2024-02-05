""""CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.
DEPOIS DISSO, MOSTRE A LISTAGEM DE NUMEROS GERADOS E TAMBEM INDIQUE O MENOR E O MAIOR VALOR QUE ESTAO NA TUPLA.
"""

from random import randint
gerador = (randint(1, 10), randint(1, 10), randint(1,10), 
           randint(1,10), randint(1,10))
print('Os valores sorteados: ', end='')
for n in gerador:
    print(f'{n} ', end='')
print(f'\n O maior valor foi {max(gerador)}')
print(f'O menor valor sorteado foi {min(gerador)}')

