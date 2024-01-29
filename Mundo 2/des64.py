""""CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. O PROGRAMA SO VAI PARAR QUANDO O USUARIO DIGITAR O VALOR 999
QUE É A CONDICAO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS FORAM DIGITADOR E QUAL FOI A SOMA ENTRE ELES
DESCONCIDERANDO O FLOG."""

nun = cont = soma = 0
num = int(input('Digite um numero ou [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1 
    num = int(input('Digite um numero ou [999 para parar:]'))
print('Voce digitou {} os valores somados sao {}'.format(cont, soma))
