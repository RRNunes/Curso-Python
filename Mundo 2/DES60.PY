""""FACA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL.
EX : 5!=5X4X3X2X1=20"""

"""from math import factorial
n = int(input('Digite valor para calcular fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.fatorial(n, f))
"""


n = int(input('Digite valor para calcular fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print(' {} '.format(c), end=' ')
    print('x' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(' {} '.format(f))
