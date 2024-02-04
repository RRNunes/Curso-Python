"""CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE AO
USUARIO QUAL SERA O VALOR A SER SACADO (NUMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CEDULAS DE CADA VALOR SERAO ENTREGUES
OBS; CONSIDERE QUE O CAIXA POSSUI CEDULAS DE R$ 50, 20, 10 E 1"""


print('===== BANCO DOS POBRES =====')
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total > 0:
             print(f'Total de {total_cedula} cedulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('-=' * 20)
print('Volte sempre ao BANCO DOS POBRES! Tenha um bom dia!')