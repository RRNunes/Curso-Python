"""CRIE UM MODULO CHAMADO moeda.py  QUE TENHA AS FUNCOES INCORPORADAS aumentar(), diminuir(),dobro() e metade().FACA TAMBEM UM PROGRAMA QUE importe ESSES MODULOS E USE ALGUMAS DESSAS FUNCOES."""

def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res

