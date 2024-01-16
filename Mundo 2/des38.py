"""Ëscreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela a mesnssagem:
- O primeiro numero é maior
- O segundo numero é maior 
- Nao existe valor maior, os os dois numero sao iguais"""

n1 = int(input('Digite primeiro valor:'))
n2 = int(input('Digite segundo valor: '))
if n1 > n2 :
    print('O primeiro é maior')
elif n2 > n1 :
    print('O segundo numero é maior')
else:
    print('Os dois numero sao iguais!')
