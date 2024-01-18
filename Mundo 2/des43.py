"""Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela a baixo
- Abaixo de 18.5: Acima do eso
- Entre 18.5 a 25: Peso ideal
- 25 ate. 30: sobrepeso
- 30 ate 40: Sobrepeso
- Acima do peso 40: Obsidade morbida"""

altura = float(input('Digite sua altura: '))
peso = float(input('Digite peso: '))
imc = (altura * 2) / peso
if imc ==18.5 <25:
    print('Peso ideal!')
elif imc <30:
    print('Acima do peso!')
elif imc <40:
    print('sobrepeso!')
else: 
    print('Obesidade morbida!')
    