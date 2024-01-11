# Faça um algoritimo que leia o prec2o de um produto e mostre o novo prec2o com 5% de desconto
p = float(input('Qual o preço do produto? R$'))
n = p - (p * 5 / 100)
print('O prec1o com deconto é R${:.2f}'.format(n))
