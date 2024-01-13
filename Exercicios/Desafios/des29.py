#Escreva um programa que leia a velocidade de um carro. 
velocidade_carro = float(input('Digite a velocidade do carro: '))
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
if velocidade_carro > 80:
    print('MULTADO! Voce ultrapassou o limite de velocidade de 80km/h.')
#A multa vai custar R$7,00 por km acima do limite
    multa = (velocidade_carro -80) * 7
    print('Sua multa é de R${}.'.format(multa))
print('Tenha um bom dia! Dirija com segurancao!')

