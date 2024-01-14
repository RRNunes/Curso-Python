#Desenvolva um programa que pergunte a distancia de uma viagem em km.
distancia_viagem = float(input('Digite a distancia da sua viagem em km: '))
#calcule o preco da passagem, cobrando R$O,50 por km para viagens ate 200km
preco = distancia_viagem *  0.50 if distancia_viagem <=200 else distancia_viagem * 0.45
print('O preco da sua viagem é R$ {:.2f}'.format(preco))