"""EX: 107:
CRIE UM MODULO CHAMADO moeda.py  QUE TENHA AS FUNCOES INCORPORADAS aumentar(), diminuir(),dobro() e metade().FACA TAMBEM UM PROGRAMA QUE importe ESSES MODULOS E USE ALGUMAS DESSAS FUNCOES.

EX 108: 
Adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado."""

def aumentar(preco, taxa = 0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa = 0):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco = 0):
    res = preco * 2
    return res


def metade(preco = 0):
    res = preco / 2
    return res


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

