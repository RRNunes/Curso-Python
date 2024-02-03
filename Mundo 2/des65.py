""""CRIE UM PROGRAMA QUE LEIA VARIOS NUMERO INTEIROS PELO TECLADO. NO FINAL DA EXECUCAO, MOSTRE A MEDIA
ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E MENOSR VALORE LIDOS. O PROGRAMA DEEVE PERGUNTAR AO USUARIO SE ELE QUER OU NAO
CONTINUAR A DIGITAR VALORES"""

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar[S/N]? ')).upper().strip()
media = soma / quant
print('Voce digitou {} numeros, a media entre eles e {}'.format(quant, media))
print('O valor foi {} e o menor foi {}'.format(maior, menor))



