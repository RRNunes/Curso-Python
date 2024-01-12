# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcula e mostre o comprimento da hipotenusa.

#co = float(input('Dijite valo do cateto oposto: '))
#ca = float(input('Digite valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa é {:.2f}'.format(hi))

from math import hypot
co = float(input('Dijite valo do cateto oposto: '))
ca = float(input('Digite valor do cateto adjacente: '))
print('O cumprimento da hipotenusa é {:.2f}'.format(hypot(co, ca)))
