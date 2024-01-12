# Fca um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.

from math import radians, sin, cos, tan
an = float(input('Digite angulo: '))
seno = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, seno))
co = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, co))
ta = tan(radians(an))
print('O angulo de {} tem como TANGENTE de {:.2f}'.format(an,ta))

