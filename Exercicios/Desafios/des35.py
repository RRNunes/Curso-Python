"""'Desemvolva um programa que leia o comprimento de 3 retas e diga ao usuario se ele pode formar um triangulo"""
print('-='*20)
print('ANALIZADOR DE TRIANGULOS')
print('-='*20)
r1 = float(input('Digite valor: '))
r2 = float(input('Digite valor: '))
r3 = float('Digite valor: ')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos PODEM FORMAR TRIANGULO')
else:
    print('Os seguimentos NAO FORMAM TRIANGULO')
