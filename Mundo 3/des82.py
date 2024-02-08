""""CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR EM UMA LISTA. DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VAO
CONTER APENAS OS VALORES PARES E VALORES IMPARES DIGITADOS, RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEUDO DAS
TRES LISTAS GERADOS."""

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
