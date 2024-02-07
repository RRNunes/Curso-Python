""""CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR VARIOS VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA.
CASO O NUMERO JA EXISTA LA DENTRO, ELE NAO SERA ADICIONADO. NO FINAL, SERAO EXIBIDOS TODOS OS 
VALORES UNICOS DIGITADOS, EM ORDEM CRESCENTE."""

numeros = list()
while True:
    n = int(input('Digite um valor : '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(' Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continumar [S/N]? '))
    if r in 'Nn':
            break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
