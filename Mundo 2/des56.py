""""DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
A MEDIA DE IDADE DO GRUPO.
QUAL O NOME DO HOMEM MAIS VELHO.
QUANTAS MULHERES TEM MENOS DE 20 ANOS."""

totalmulher = 0
maioridadehomem = 0
mediaidade = 0
homemvelho = ' '
somaidade = 0
for p in range(1, 5):
    print(' {} pessoa'.format(p))
    nome = str(input('Digite nome: ')).strip()
    idade = int(input('Digite idade: '))
    sexo = str(input('Digite sexo F/M : ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if  sexo in 'Ff' and idade < 20:
        totalmulher += 1
    mediaidade = somaidade / 4
print('A maior idade do grupo é {} anos'.format(mediaidade))
print('O mais velho é {} e tem {}'.format(homemvelho, maioridadehomem))
print('{} tem menos de 20 anos'.format(totalmulher))

