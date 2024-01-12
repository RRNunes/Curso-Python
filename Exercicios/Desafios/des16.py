# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porcao inteira.
#Ex: Digiteum número: 6.127
#O número 6.127 tem a parte inteira 6

#from math import trunc
#n = float(input('Digite valor: '))
#print('O valor digitado foi {} e a sua parte inteira é {}.'.format(n, trunc(n)))

n = float(input('Digite valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(n, int(n)))
