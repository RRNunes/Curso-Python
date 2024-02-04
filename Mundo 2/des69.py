"""CRIE UM PROGRAMA A IDADE E O SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA,
O PROGRAMA DEVERA PERGUNTAR SE O USUARIO QUER OU NAO CONTINUAR. NO FIMAL, MOSTRE:
a) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
b) QUANTOS HOMENSFORAM CADASTRADOS
c) QUANTAS MULHERES TEM ENOS DE 20 ANOS."""

print('===== BANCO DE DADOS =====')
total_18 = total_homen = total_mulher20 = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = ' '
    while sexo not in 'MF':
        print('-' * 30)
        sexo = str(input('Digite sexo [F/M]: ')).strip().upper()
    if idade >= 18:
        total_18 += 1 
    if sexo == 'M':
        total_homen += 1
    if sexo == 'F' and idade < 20:
        total_mulher20 += 1
    resposta = ' '
    while resposta not in 'S/N':
        print('-' * 30)
        resposta = str(input('Quer continuar [S/N]?')).strip().upper()
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Total de pessoas com mais de 18  anos: {total_18}')
print(f'Ao todo temos {total_homen} homens cadastrados')
print(f'E temos {total_mulher20} mulhere com menos de 20 anos')

