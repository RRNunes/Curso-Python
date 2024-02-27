"""CRIE UM PROGRAMA QUE TENHA UMA FUNCAO FATORIAL() QUE RECEBA DOIS PARAMETROS: O PRIMEIRO QUE INDIQUE O NUMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERA UM VALOR LOGICO(OPCIONAL) INDICADO SE SERA MOSTRADO OU NAO NA TELA O PROCESSO DE CALCULO DO FATORIAL.
"""

def fatorial(n, show=False):
    f = 1 
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f += c
    return f


print(fatorial(5, show=True))