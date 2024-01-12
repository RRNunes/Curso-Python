# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos e mostrar a ordem sorteada

from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A orde de apresentacao sera: ')
print(lista)
