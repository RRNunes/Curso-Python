""""CRIE UM PROGRAMA ONDE O USUARIO DIGITE UMA EXPRESSAO QUALQUER QUE USE PARENTESES. SEU APLICATIVO DEVERA
ANALISAR SE A EXPRESSAO PASSADA ESTA COM OS PARENTESES ABERTOS E FECHADOS NA OR DEM CORRETA."""

expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '()':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
    