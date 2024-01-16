"""Escreva um programa para aprovar o emprestimo bancario para  a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado"""

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
ano = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (ano * 12)
minimo = salario *30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano))
print('A prestacao sera de R4{:.2f}'.format(prestacao))
if prestacao <= salario:
    print('Emprestimo APROVADO!!!')
else:
    print('Emprestimo NEGADO!!!')
    