""""Faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""
ano = int(input('Digite ano: '))
calculo = ano % 4
if calculo == 0:
    print('O ano {} é bissexto.'.format(ano))
else: 
    print('O ano {} nao é bissexto.'.format(ano))
