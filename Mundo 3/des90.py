""""DESAFIO: 90: DICIONARIOS EM PYTHON

FACA UM PROGRAMA QUE LEIA NOME E MEDIA DE UM ALUNO, GUARDANDO TAMBEM A SITUACAO
EM UM DICIONARIO. NO FINAL, MOSTREE O CONTEUDO DA ESTRUTURA NA TELA.
"""

aluno = dict()
aluno['Nome'] = str(input('nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
aluno['Situacao'] = 'Aprovado' if aluno['Media'] >= 7 else 'Reprovado'
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
    