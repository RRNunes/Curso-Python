""""CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS 
[ 5 ] SAIR DO PROGRAMA

SEU PROGRAMA DEVERA REALIZAR A OPERACAO SOLICITADA EM CADA CASO"""

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ]somar
    [ 2 ]multiplica
    [ 3 ]maior
    [ 4 ]novos numeros
    [ 5 ]sair do programa''')
    opcao = int(input('Qual sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('O resultado de {} + {} e {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicacao de {} x {} é {}'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Ente {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numero novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO..')
        sleep(1)
    else:
        print('Opcao invalida. Tente novamente.')
print('FIM DO PROGRAMA!')
