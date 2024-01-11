# Crie um programa que leia quanto a pessoa tem na carteira e mostre quantos dolares ela pode comprar, CONSIDERANDO O DOLAR $3,57
real = float(input('Digite quanto diheiro você tem na cateira: R$')) 
dolar = real * 3.27
print('Com R${:.2f} você pode comprar ${:.2f} dolares.'.format(real, dolar)) 

