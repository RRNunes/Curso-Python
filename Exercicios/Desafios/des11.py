# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessaria para pintar, sabendo que cada lata de tinta pinta uma área de 2mm2
altura = float(input('Digite a altura de sua parede: ')) 
largura = float(input('Digite a largura de sua parede: ')) 
area = altura * largura
print('A area total de sua é {}m2'.format(area)) 
tinta = area / 2
print('Para pintar a parede necessario {}l de tinta'.format(tinta)) 
