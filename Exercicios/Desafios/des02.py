# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

d = int(input('Que dia você nasceu?'))
m = input('Qual o mes que você nasceu?')
a = int(input('Qual seu ano de nascimento?'))
print('Você nasceu no dia {} de {} de {}. Correto?'.format(d, m, a)) 
