# Crie um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece o(a)
#Em que posicao ela aparece a primeira vez
# Em que posicao aparece pela ultima vez

frase = input('Digite uma frase: ').upper().strip()
print('Quantas vezes aparece a letra A na frase? {}'.format(frase.count('A')))
print('A primeira letra A aparece na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na possicao {}'.format(frase.rfind('A')+1))
