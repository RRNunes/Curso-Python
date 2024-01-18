"""Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela a baixo
- Abaixo de 18.5: Acima do eso
- Entre 18.5 a 25: Peso ideal
- 25 ate. 30: sobrepeso
- 30 ate 40: Sobrepeso
- Acima do peso 40: Obsidade morbida"""

altura = float(input('Digite sua altura:  (m)'))
peso = float(input('Digite peso: (kg)'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif 18.5 <= imc <25:
    print('Seu peso é!')
elif 25 <= imc < 30:
    print('sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidae!!!')
else: 
    print('Obesidade morbida!')
print('O seu IMC é {:.1f}'.format(imc))
    