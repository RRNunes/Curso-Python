"""
Faca um algoritmo que ordene uma lista de numeros inteiros aleatorios

Exemplo:
  In:  [1, 4, 2, 8, -3, 5]
  Out: [-3, 1, 2, 4, 5, 8]

Nao pode usar sort()
"""


# Escreva seu codigo aqui
def my_sort(input: list):
    return input


if __name__ == '__main__':
    input = [1, 4, 2, 5, 3]
    output = my_sort(input)
    assert output == sorted(input)
    print(f"Parabens! Resultado: {output}")
