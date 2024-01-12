# Um professor quer sortear um dos seus alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome de escolhido

from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Digite quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
