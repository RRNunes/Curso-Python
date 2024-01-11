#Crie um script Python que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

d = int(input('Que dia voce nasceu?'))
m = input('Qual o mes que voce nasceu?')
a = int(input('Qual seu ano de nascimento?'))
print('Voce nasceu no dia {} de {} de {}. Correto?'.format(d, m, a)) 
