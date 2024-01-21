""""DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA pa. nO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSAO"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' ')
print('ACABOU!')
