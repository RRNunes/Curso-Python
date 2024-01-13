# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome (Santo)

nome_cidade = (input('Digite o nome de uma cidade: '))
print('A cidade comesa com Santo? {}'.format('santo' in nome_cidade.lower()))