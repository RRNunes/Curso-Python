"""
Exercício Python 113:
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! por favor, digite um numero inteiro valido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados foi interrompida pelo usuario.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! por favor, digite um numero inteiro valido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados foi interrompida pelo usuario. ')
            return 0
        else: 
            return n
        

num1 = leiaInt('Digite um valor: ')
num2 = leiaFloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}.')

