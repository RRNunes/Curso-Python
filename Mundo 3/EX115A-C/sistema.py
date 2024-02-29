from interface import *
from time import sleep
from lib import *

arq = 'Cursoem video.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo nao existe')

    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opcao 1')
    elif resposta == 2:
        cabecalho('Opcao 2')
    elif resposta == 3:
        cabecalho('Sainado do sistema...Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao invalida!\033[m')
        sleep(2)

