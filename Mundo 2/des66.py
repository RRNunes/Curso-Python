"""Crie um programa que leia varios numeros inteiro pelo teclado.O programa so vai parar quando
o usuario digitar o valor 999, que e sua condicao de parada. No final, mostre quantos numeros
foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

soma = cont = 0
while True:
    numero = int(input('Digite um numero inteiro ou [999 PARA PARAR]:'))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Voce digitou {cont} e a soma entre eles e {soma}')
