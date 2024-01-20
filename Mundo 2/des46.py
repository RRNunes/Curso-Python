""""Face um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio
indo de 10 ate 0, com uma pausa de um segundo"""

from time import sleep
for cont in range(10, -1, -1):
   print(cont)
   sleep(1)
print('PARAPAPA POWWWW!')