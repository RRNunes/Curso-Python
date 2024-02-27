"""FACA UM MINI-SISTEMA QUE ULTILIZE O INTERACTIVE HELP DO PYTHON.
O USUARIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO O USUARIO DIGITAR A PALAVRA ''SIM, O PROGRAMA SE ENCERRARA.
OBS: USE CORES.
"""

c = ('\033[m',       # 0 - sem cores
     '\033[0;30;41m' # 1 - vermelho
     );

def ajuda(com):
    titulo(f'Acessando manual do comando \'{com} \'', 4)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Funcoes ou Bliblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)