""""DESEMVOLVAA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-O EM UMA TUPLA
NO FINAL , MOSTRE:

A) QUANTAS VEZES APARECEU O VALOR 9.
B) EM QUE POSICAO FOI DIGITADO O PRIMEIRO VALOR 3.
C) QUAIS FORAM OS NUMERO PARES.
"""

numero = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite mais um numero: ')),
          int(input('Digite outro numero:')))
print(f'Voce digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}a posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
