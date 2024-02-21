""" EXERCICIO 092: cadastro de trabalhador em python

crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre - os (com idade) em um dicionario. se por acaso a CTPS FOR DIFERENTE DE ZERO, O DICIONARIO RECEBERA TAMBEM O ANO DE CONTRATACAO E O SALARIO.
CALCULE E ACRESCENTE, ALEM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
"""

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35)) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

