#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um valor: ')) 
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), pow(n, (1/2)))) 

