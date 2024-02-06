""""CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTO PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATE VINTE
SEU PROGRAMA DEVERA LER UM NUMERO PELO TECLADO (0 E 20 ) E ESCREVA POR EXTENSO"""

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 'nove', 
            'dez', 'ónze', 'doze', 'treze', 'quatorze', 
            'quize', 'dezessseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente... ', end='')
print(f'Voce digitou o numero {contagem[numero]}')

