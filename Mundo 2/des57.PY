""""FACA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAIS SO ACEITE M OU F. CASO ESTEJA ERRADO PECA A DIGITACAO
NOVAMENTE ATE TER UM VALOR CORRETO"""

sexo = str(input('Informe seu sexo: M/F ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
