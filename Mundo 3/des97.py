"""FACA UM PROGRAMA QUE TENHA UMA FUNCAO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARAMETRO E MOSTRE UMA MENSAGEM COM TAMANHA ADAPTAVEL.
eX: escreva('Ola Mndo!')
Saida:
----------
Ola Mundo!
---------- 
"""

def escreva(msg):
    tam = len(msg) + 4 
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva('Katyanne Roberta')
escreva('Curso Python')
escreva('Curso em video')
