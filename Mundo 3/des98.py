"""faca um programa que tenha uma funcao chamada contador(), que receba tres parametros: inicio, fim, e passo. SEU 
PROGRAMA TEM QUE REALIZAR TRES CONTAGENS ATRAVEZ DA FUNCAO CRIADA:
A) DE 1 ATE 10, DE 1 EM 1
B) DE 10 ATE 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA.
"""

from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(0.5)

    if p < 0:
        p*= -1
    if p == 0:
        p = 1 
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i 
        while cont >= f:
            print(f' {cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Agora e sua vez de personalizar a contagem.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
