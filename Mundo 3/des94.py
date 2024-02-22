"""EXERCICIO 94: UNINDO DICONARIOS E LISTAS 

CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO E TODOS OS DICIONARIOS EM UMA LISTA. NO FINAL, MOSTRE: 

A) QUANTAS PESSOAS CADASTRADAS.
B) A MEDIDA DE IDADE.
C) UMA LISTA COM MULHERES.
D) UMA LISTA COM IDADE ACIMA DA MEDIA.
 """

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? '))
        if resp in 'SsNn':
            break
        print('Erro! Por favor apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
    print()
    print('D) Lista das pessoas que estao acima da media: ' )
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< encerrando >>')
