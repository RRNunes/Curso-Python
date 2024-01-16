""""Faca um programa que elia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele ainda vai se alistar no servico militar
- Se é a hora de se alistar
- Seja passou do tempo do alistamento
Seu programa tem devera mostrar o tempo que falta ou se passou do prazo"""

from datetime import date
atual = date.today().year
dn = int(input('Digite seu ano de nascimento: '))
idade = atual - dn
print('Quem nasceu em {} tem {} anos em {}'.format(dn, idade, atual))
if idade == 18 :
    print('Voce tem que se alistyar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voce voce ainda nao tem 18 anos. Ainda faltam {} para o alistamento'.format(saldo))
    print('Seu alistamento se {}'.format(ano))

elif idade >18: 
    saldo = idade - 18
    ano = atual - saldo
    print('Voce ja deveria ter se alistado a {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))

