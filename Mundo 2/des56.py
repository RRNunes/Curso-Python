""""DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
A MEDIA DE IDADE DO GRUPO.
QUAL O NOME DO HOMEM MAIS VELHO.
QUANTAS MULHERES TEM MENOS DE 20 ANOS."""

somaidade = 0
for p in range(1, 5):
    print(' {}pessoa'.format(p))
    nome = str(input('Digite nome: ')).strip()
    idade = int(input('Digite idade: '))
    sexo = str(input('Digite sexo F/M : ')).strip()
    somaidade += idade

