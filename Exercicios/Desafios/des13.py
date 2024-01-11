# Fac1a um algoritimo que calcule o almento de 15% no salario dos funcionarios
s = float(input('Digite salario: R$'))
ns = s + (s * 15 / 100)
print('O novo salario é R${:.2f}'.format(ns)) 
