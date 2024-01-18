"""Elabore um prohgrama que calcule um valor a ser pago por um produto. considerando:
-  a vista dinheiro/cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- am ate 2x no cartao: preco normal
- 3x ou mais no cartao 20% de juros"""

preco = float(input('Digite valor: R$ '))
print('''Escolha forma de pagamentp
[1] Dinheiro / cheque
[2] A vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = int(input('Digite sua opcao: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco 
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input('Digite numero de parcelas: '))
    parcela = total / totalparcela
    print('O valor total em {}x é R${} com juros'.format(totalparcela, parcela))
else:
    print('Opcao invalida!')
print('Sua compra de R${} tem o valor final de R${}'.format(preco, total))

