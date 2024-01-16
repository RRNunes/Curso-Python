"""Ä confederacao nacional de natacao precisa de um programa que leia o ano de nescimento de 
um atleta e mostre sua categoria, de acordo com a idade:
- Ate 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos : JUNIOR
- Ate 20 anos:  SENIOR
aCIMA: MASTER """

from datetime import date
atual = date.today().year
ano = int(input('Digite ano: '))
idade = atual - ano
print('A idade é {}'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif  idade <= 19:
    print('JUNIOR')
elif idade <=20:
    print('SENIOR')
else:
    print('MASTER')
