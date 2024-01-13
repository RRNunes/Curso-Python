# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo cada uma tem(sem considerar os espaços)
# Quantas letras tem o primeiro nome

n = input('Qual seu nome completo? ')
print('O nome maiúsculo é:')
print(n.upper())
print('O nome minúsculo é:')
print(n.lower())
tamanho_string = len(n)
qt_espaco_branco = n.count(' ')
print(f"t: {tamanho_string}, qsb: {qt_espaco_branco}")
qt_letras = tamanho_string - qt_espaco_branco
print('Seu nome tem {} caracteres:'.format(qt_letras))
s = (n.split())
print('Seu primeiro nome {} tem {} caracteres'.format(s[0], len(s[0]))) 