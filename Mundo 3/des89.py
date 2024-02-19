""""CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VARIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA,
NO FINAL, MOSTRE UM BOLETIM CONTENDO A MEDIA DE CADA UM E PERMITA QUE O USUARIO POSSA MOSTRAR AS  NOTAS DE CADA ALUDO INDIVIDUALMENTE.
 """

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1; '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar [S/N]? '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar notas de qual aluno(999 interrompe)?'))
    if opc == 999:
        print('FINALIZANDO...')
        break
        if opc <= len(ficha) - 1 :
            print(f'Notas de {ficha[opc][0]} sao {fichas[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
    