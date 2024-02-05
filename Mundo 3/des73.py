""""crie uma tupla preenchida com os 20 primeiros colocador da tabela
do campeonato brasileiro de futebol, na ordem de colocacao.
depois mostre:

a) OS 5 PRIMEIROS .
B) OS ULTIMOS 4 COLOCADOS.
C) TIMES EM ORDEM ALFABETICA.
D) EM QUAL POSICAO ESTA O TIME DA CHAPECOENSE.
"""
div = ('-=' * 30)
times = ('Corintians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atletioco', 'Botafogo', 
         'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife', 
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Átletico-GO')
print(div)
print(f'Lista de times do Brasileirao: {times}')
print(div)
print(f'Os 5 primeiros sao {times[0:5]}')
print(div)
print(f'Os 4 ultimos sao {times[-4:]}')
print(div)
print(f'Times em ordem alfabetica: {sorted(times)}')
print(div)
print(f'O chapecoense esta na {times.index("Chapecoense")+1}a posicao')

