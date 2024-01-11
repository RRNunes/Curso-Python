# Escreva um programa que leia um valor em metros e o exbiba convertido em centimetros e milimetros.
v = float(input('Digite medida: ')) 
cm = v * 100
mm = v *1000
print('A medida é {:.0f}cm \n A medida é {:.0f}mm'.format(cm, mm))

