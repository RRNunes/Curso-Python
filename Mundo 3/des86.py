""""CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIVISAO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO.

0 [_][_][_
1[_][_][_]
0     1

NO FINAL, MOSTE A MATRIZ NA TELA, COM A FORMATACAO CORRETA"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[1][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
