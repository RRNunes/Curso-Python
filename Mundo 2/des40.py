""""Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma menssagem
no final de acordo com a media atingida:
- Media abaixo da 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media 7.0 ou superio: APROVADO"""

nota_1 = float(input('Digite primeira nota: '))
nota_2 = float(input('Digite segunda nota: '))
media = (nota_1 + nota_2) / 2
print('Tirando {} e {}, a media do aluno é {}'.format(nota_1, nota_2, media))
if media <= 5:
    print('Voce foi REPROVADO!')
elif media < 7:
    print('Voce esta de RECUPERACAO!')
else:
    print('PPARABENS VOCE FOI APROVADO!')

