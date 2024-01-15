#Ëscreva um programa que pergunte o salario de um funcionario
salario = float(input('Digite salario: R$'))
# e camcule o valor do seu. aumento.
#para salarios superiores a 1.250 10% de aumento, para salario inferio 15%
if salario <=1.250 : 
    s1 = salario + (salario *15 / 100)
else: 
    s1 = salario + (salario *10 / 100)
print('O novo salario sera de R${:.2f}'.format(s1))
