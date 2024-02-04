"""CRIE UM PROGRAMA QUE LEIA O NOME E O PRECO DE VARIOS PRODUTOS. O PROGRAMA
DEVERA PERGUNTAR SE O USUARIO VAI CONTINUAR. NO FINAL, MOSTRE:
A) QUAL E O TOTAL GASTO NA COMPRA
B) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
C) QUAL 'E O PRODUTO MAIS BARATOI"""

print('====== CADASTRO DE COMPRA ======')
total = totalmaior = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto'))
    preco = float(input('Preco: R$ '))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    total += preco
    if preco > 1000:
        totalmaior += 1
    resposta = ' '
    while resposta not in 'SN':
        print('-' * 30)
        resposta = str(input('Quer continuar [S/N?')).strip().upper()[0]
    if resposta == 'N':
        break
    print('-' * 30)
print(f'FIM')
print('-=' * 30)
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totalmaior} que custaram mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')