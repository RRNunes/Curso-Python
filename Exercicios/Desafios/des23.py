# Faça um programa que leia um número de 0 a 9999 e mostre na. tela cada um dos digitos separados.
# ex:
#Digite um numero: 1834
#uninade: 4
#dezena:3
#centena:8
#milhar:1

numero = (input('Digite um valor:'))
dividido = numero
print('Ánalisando o numero {}'.format(numero))
print('Unidade:{}'.format(dividido[3]))
print('Dezena: {}'.format(dividido[2]))
print('Centena:{}'.format(dividido[1]))
print('Milhar: {}'.format(dividido[0]))
