from moeda import metade, dobro, aumentar

p = float(input('Digite o preco: R$ '))
print(f'A metade de {p} e {metade(p)}')
print(f'O dobro de R${p} e R${dobro(p)}')
print(f'Aumentar 10%, temos R${aumentar(p, 10)}')

