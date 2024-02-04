"""FACA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS, UM DE CADA VEZ, PARA CADA VALOR GIGITADO
PEELO USUARIO. O PROGRAMA SERA INTEROMPIDO QUANDO O  NUMERO SOLICITADO FOR NEGATIVO"""

print('==== TABUADA =====')
while True:
    tabuada = int(input('Digite numero: '))
    print('=' * 20)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c:2} = {tabuada * c}')
    print('=' * 20)
print('PROGRAMA TABUADA ENVCERRANDO. VOLTE SEMORE!')
