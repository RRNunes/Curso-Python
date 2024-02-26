"""EXERCICIO 95: APRIMORANDO OS DICIONARIOS

APRIMORE O EXERCICIO 93 PARA QUE ELE FUNCIONE COM VARIOS JOGADORES, INCLUINDO UM SITEMA
DE VISUALIZACAO DE DETALHES DE APROVEITAMENTO DE CADA JOGO."""

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]?'))
        if resp in 'SsNn':
            break
        print('Erro! Responda apenas S ou N.')
        if resp =='Nn':
            break
    print('-=' * 30)
    print('cod ', end='')
    for i in jogador.keys():
        print(f'{i:<15} ', end='')
    print()
    print('-=' * 30)
    for k, v in enumerate(time):
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
            print()
        print('-=' * 40)
        
