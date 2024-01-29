""""MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS . O PROGRAMA
ENCERRA QUANDO ELE SISSER QUE QUER MOSTRAR O TERMO."""


print('GERADOR DE PA')
print('-='* 10)
primeiro = int(input('Divite termo: '))
razao = int(input('Razao PA: '))
termo = primeiro
cont = 1
while cont <10 :
    print(' {} = '.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM!')
