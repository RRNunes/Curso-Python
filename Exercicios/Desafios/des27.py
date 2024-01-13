# Faca um programa que leia o nome de uma pessoa. mostre em seguida o primeiro e o ultimo nome separadamente.

nome_completo = input('Qual seu nome completo? ').strip()
nome = nome_completo.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é? {}'.format(nome[len(nome) - 1]))
