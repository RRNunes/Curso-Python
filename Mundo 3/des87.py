"""APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:

A) A SEMA DE TODOS OS VALORES PARES DIGITADO.
B) A SOMA DOS VALORES DA TERCEIRA COLUNA
C) O MAIOR VALOR DA SEGUNDA LINHA.
"""

matriz = [[0, 0, 0], [0, 0, ], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l[c]] = int(input(f'Digite um valor para [{1}, {c}]: '))
print('-=' * 3)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}', end='')
for l in range(0, 3):
    scol += matriz[l][c]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

