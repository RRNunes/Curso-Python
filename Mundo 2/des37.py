"""Éscreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual
sera a base de conversao
1 para binario
2 para octal
3 para hexadecimal"""

numero = int(input('Digite um numero inteir: '))
print('Para converter digite 1 para binari, 2 para octal e 3 para  hexadecimal: ')
op = int(input('Sua o opcao: '))
if op == 1 :
    print('Numero {} convertido para binario é {}'.format(numero, bin(numero[2:])))
elif op == 2 :
    print('Numero {} convertido para octal é {}'.format(numero, oct(numero[2:])))
elif op == 3 :
    print('Numero {} convertido para hexadecimal é {}'.format(numero, hex(numero[2:])))
else:
    print('Opcao invalida, tente novamente: ')
    


