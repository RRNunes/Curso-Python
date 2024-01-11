#EXERCICIO 04
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e tdsnasninformacoes possiveis sobre ela
d = input('Digite algo: ')
print('O tipo primitivo desse valor é: ' ,type(d))
print('É um número? ', d.isnumeric())
print('É um alfanúmerico? ', d.isalnum()) 
print('É Maiúscolo? ', d.isalpha()) 