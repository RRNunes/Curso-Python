""""CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PRECOS
NA SEQUENCIA, NO FINAAL, MOSTRE UMA LISTAGEM DE PRECOS, ORGANIZADO OS DATOS EM FORMA TABULAR.
"""

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Estojo', 15.9,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-' * 40)
print('======== LISTAGEM DE PRECO ========')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
