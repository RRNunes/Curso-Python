# Escreva um programa que pergunnte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado. 

km = float(input('Quantos km foram percorridos: '))
d  = int(input('Quantos dias de aluguel: '))
c1 = km * 0.15
c2 = d * 60
t  = c1 + c2
print('O valor do km rodade é R${:.2f} \n. O valor dos dias de aluguel sao R${:.2f} \n. O total a pagar é R${:.2f}.'.format(c1, c2, t))

