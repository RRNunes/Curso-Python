""""REFACA O DESAFIO 9, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SO QUE AGORA ULTILIZANDO UM LACO"""

n = int(input('Digite numero: '))
for c in range(1, 11):
    print('{} x {:.2f} = {}'.format(n, c, n * c))
print('FIM')
