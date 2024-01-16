""""Refaca o desafio 035 dos triangulod, acrecentando recursos ce mostrar ue tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Ioscales: dois lados iguais 
- Escaleno: todos os lado iguais"""


print('ANALIZADOR DE TRIANGULOS')
r1 = float(input('Digite valor: '))
r2 = float(input('Digite valor: '))
r3 = float(input('Digite valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos PODEM FORMAR UM TRIANGULO')
    if r1 == r2 == r3:
        print('EQUILATERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR UM TRIANGULO')
    
