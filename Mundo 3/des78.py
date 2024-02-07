""""FACA UM PROGRAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE-OS EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS
POSICOES NA LISTA."""
maior = 0
menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posicao {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 30)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor é {maior} nas posicoes ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()



