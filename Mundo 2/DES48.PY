""""fACA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES
E QUE SE ENCONTRAM NO INTERVALO DE 1 ATE 500."""

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A SOMA DE TODOS OS {} VALORES SOLICITADOS É {}'.format(cont, soma))  