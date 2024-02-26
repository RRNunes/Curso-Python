"""
Faca um algoritmo que ordene uma lista de numeros inteiros aleatorios

Exemplo:
  In:  [1, 4, 2, 8, -3, 5]
  Out: [-3, 1, 2, 4, 5, 8]

Nao pode usar sort()
"""


# Escreva seu codigo aqui
def my_sort(input):
    for i in range(len(input)): 
      for cont in range(0, len(input)-i-1):
         if input[cont] > input[cont+1]:
            input[cont], input[cont+1] = input[cont+1], input[cont]
    return input


if __name__ == '__main__':
    input = [1, 4, 2, 5, 3]
    output = my_sort(input)
    assert output == sorted(input)
    print(f"Parabens! Resultado: {output}")
