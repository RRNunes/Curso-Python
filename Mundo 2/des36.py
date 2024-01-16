"""Escreva um programa para aprovar o emprestimo bancario para  a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado"""
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
ano = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / ano
if prestacao > salario + (salario *30//100):
    print('Seu emprestino nao foi aprovado!')
elif prestacao <= salario + (salario *30//100):
    print('Seu emprestimo foi aprovado!')
else:
    total = prestacao + salario
    print('Seu financiamento tera o valor total de R${}. Parabens!'.format(total))
    