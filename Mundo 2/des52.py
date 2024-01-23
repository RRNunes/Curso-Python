"""""FACE UM PROGRAMA QUE LEIA UM NU ERO INTEIRO E DIGA SE ELE É OU NAO UM NUMERO PRIMO."""

numero = int(input('Dige um valor: '))
tot = 0
for c in range(1, numero + 1 ):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso É PRIMO')
else:
    print('E por isso ele NAO É PRIMO')
    