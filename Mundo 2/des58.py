""""MELHORE O JOGO DO DESAFIO 28 ANDE O COMPUTADOR VAI PENSAR EM UM NUMERO DE 0 A 10. SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATE ACERTAR O NUMERO QUE O
O COMPUTADOR ESCOLHEU EM QUANTOS PALPITES FOREM NECESSARIOS"""

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos ...Tente mais uma vez.')
print ('Acertou com {} tentativas. PARABENS!'.format(palpite))

