"""EXERCICIO 093: CADASTRO DE JOGADOR DE FUTEBOL

CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DE JOGADOR
E QUANTAS PARTIDADS ELE JOGOU. PEDOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO SERA GUARDADO EM UM DICIONARIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.

"""

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida.')
for k, v in enumerate(jogador['gols']):
    print(f'  => ')