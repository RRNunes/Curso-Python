""""CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR EM UMA LISTA. DEPOIS
DISSO, MOSTRE:

A) QUANTOS NUMEROS FORAM DIGITADOS.
B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
C) SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA."""

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores eem ordem decrescente sao {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')
    