"""
EX: 107:
CRIE UM MODULO CHAMADO moeda.py  QUE TENHA AS FUNCOES INCORPORADAS aumentar(), diminuir(),dobro() e metade().FACA TAMBEM UM PROGRAMA QUE importe ESSES MODULOS E USE ALGUMAS DESSAS FUNCOES.

EX 108: 
Adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.

EX 109:
MODIFIQUE AS FUNCOES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARAMETRO A MAIS, INFORMANDO SE O VALOR RETORNADO PARA ELAS VAI SER OU NAO FORMATADAOS PELA FUNCAO MOEDA(), DESENVOLVIDA NO DESAFIO 108.

EX 110:
ADICIONE AO MEDULO MOEDA.PY CRIANDO NOS DESafios anteriores, uma funcao chamada resumo() QUE MOSTRE NA TELA ALGUMAS INFORMACOES GERADAS PELAS FUNCOES QUE JA TEMOS NO MODULO CRIADO ATE AQUI.

"""

def aumentar(preco, taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(preco)


def diminuir(preco, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco = 0, formato=False):
    res = preco / 2
    return res if  not formato else moeda(res)


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analizado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de reducao: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)

