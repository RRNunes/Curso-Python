"""FACA UM PROGRAMA QUE TENHA UMA FUNCAO NOTAS() QUE PODE RECEBER VARIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONARIO COM OS SEGUINTES INFORMACOES:
- QUANTIDADE DE NOTAS
- MAIOR NOTA
- A MENOR NOTA
- A MEDIA DA TURMA
- A SITUACAO(OPCIONAL)
ADICIONE TAMBEM AS DOCSTRINGS.
"""


def notas(*n, sit=False):
    """Funcao para analizar notas e situacao de varios alunos...
    ...
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'Ruim'
    return r
 

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
#help(notas)