#crie um programa que leia um numero inteiro
numero = int(input('Digite um numero: '))
#mostre na tela se ele é PAR ou IMPAR.
soma = numero % 2
if soma == 0 :
    print('O numero {} é par.'.format(numero))
else:
    print('O numero {} é IMPAR.'.format(numero))
