""""CRIE UM PROGRAMA QUE LEIA VARIOS NUMERO INTEIROS PELO TECLADO. NO FINAL DA EXECUCAO, MOSTRE A MEDIA
ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E MENOSR VALORE LIDOS. O PROGRAMA DEEVE PERGUNTAR AO USUARIO SE ELE QUER OU NAO
CONTINUAR A DIGITAR VALORES"""

menor = 0
maior = 0
media = 0
num = 0
inteiro = 0
inteiro = int(input('Digite um numero ou 999 para finalizar: '))
while num != 999:
    inteiro = int(input('Digite um numero ou 999 para finalizar: '))
    media = (inteiro + inteiro) % num
    print('FIM!')
print('Foram digitados {} numero, a media entre eles e {}'.format(num, media))



