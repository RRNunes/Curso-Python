""""REFACA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS
DA PROGERSSAO USADO A ESTRUTURA WHILE."""


print('GERADOR DE PA')
print('-=' *10)
primeiro = int(input('Digite termo: '))
razao = int(input('Razao DA PA: '))
termo = primeiro
cont = 1 
while cont <= 10 :
    print(' {} = '.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM!')

