""""FACA UM PROGRAMA QUE TENHA UMA FUNCAO CHAMADA AREA(), QUE RECEBA DIMENSOES DE UM
TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A AREADO TERRENO
"""

def area(larg, compr):
    a = larg * compr
    print(f'A area de um terreno {larg}x{compr} e de {a}m2.')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
