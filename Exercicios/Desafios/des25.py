# Crie um programa que leia o nome de uma pessoa e diga se ela tem (Silva) no nome

nome = input('Qual o seu nome: ')
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))