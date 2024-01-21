""""DESENVOLVA UM PROGRAMA QUE LEIA E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO
FOR IMPAR, DESCONCIDERE-O"""

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1 
print('Voce informou {} numero e a soma foi {}'.format(cont, soma))