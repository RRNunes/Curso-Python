"""FACA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SO SERA INTERROMPIDO QUANDO O
JOGADOR PERDER, MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO."""


from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-=' * 20)
vezes = 0
while True:
    jogador = int(input('Digite valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    pi = ' '
    while pi not in 'PI':
        pi = str(input('PARAR ou IMPAR [P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jogador}  o computador {computador}. Total de {total}')
    if total % 2 == 0:
        print('DEU PAR!') 
    else:
        print('DEU IMPAR!')
    print('-=' * 20)
    if pi == 'P':
        if total % 2 == 0:
            print('Voce GANHOU...')
            vezes += 1
        else:
            print('Voce PERDEU!')
        break
    elif pi == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            vezes += 1
        else:
            print('Voce PERDEU!')
            break
    print('-=' * 20)
    print('Vamos jogar novamente...')
print('-=' * 20)
print(f'Voce ganhou {vezes} vezes.')

