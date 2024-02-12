""""crie um programa onde o usuario possa digitar sete valores numericos e cadastra-se em uma lista unica que mantenha
separados os valores pares e impares. no final, mostre os valores pares e impares em ordem crescente."""

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
