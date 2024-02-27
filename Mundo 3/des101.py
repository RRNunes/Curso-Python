"""CRIE UM PROGRAMA QUE TENHA UMA FUNCCAO CHAMADA VOTO QUE VAI RECEBER COMO PARAMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO SE ESSA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATORIO NAS ELEICOES.
"""

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBBRIGATORIO.'
    

nasc = int(input("Em que ano voce nasceu? "))
print(voto(nasc))