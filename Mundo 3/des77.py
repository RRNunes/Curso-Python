""""CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS(NAO USAR ACENTOS).
DEPOIS DISSO,VOCE DEVE MOSTRAR, P-ARA CADA PALAVRA, QUAIS SAO AS SUAS VOGAIS.
"""

palavras = ('aprender', 'programar', 'linguajem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')


for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


