"""FACA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SO SERA INTERROMPIDO QUANDO O
JOGADOR PERDER, MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO."""


from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-=' * 20)
pontos = 0
while True:
    jogador = int(input('Digite valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    pi = ' '
    while pi not in 'PI':
        pi = str(input('PARAR ou IMPAR [P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jogador}  o computador {computador}. Total de {total}', end=' ')
    if total % 2 == 0:
        print('DEU PAR!') 
        rodada = 'p'
    else:
        print('DEU IMPAR!')
        rodada = 'i'
    print('-=' * 20)
    if pi == rodada:
        print('Voce GANHOU...')
        print('Vamos jogar novamente...')
        print('-=' * 20)
        pontos += 1
    else:
        print('Voce PERDEU!')
        break
print('-=' * 20)
print('GAME OVER!')
if pontos == 0:
    print('Voce nao ganhou nenhuma vez.')
elif pontos == 1:
    print('Voce ganhou somente 1 vez.')
else:
    print(f'Voce ganhou {pontos} vezes.')

