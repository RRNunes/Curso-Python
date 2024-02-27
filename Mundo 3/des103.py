"""FACA UM PROGRAMA QUE TENHA UMA FUNCAO CHAMADA FICHA(), QUE RECEBA DOIS PARAMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU. O PROGRAMA DEVERA SER CAPAZ DE MOSTRAR O FICHA DO JOGADOR, MESMO QUE ALGUN DADO NAO TENHA SIDO INFORMADO CORRETAMENTE.
"""

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')




n = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)




