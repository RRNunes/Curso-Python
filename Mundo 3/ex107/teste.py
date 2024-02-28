import moeda 

p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')

