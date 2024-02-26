"""
Faca um programa que retorne o fatorial de um numero.

Fatorial de um numero eh ele vezes seus numeros anteriores ate' 1:

1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
n! = 1 * 2 * 3 * ... * (n - 1) * n

Dica: Se voce prestar atencao, a expressao acima pode ser simplificada:
  - 4! = 1 * 2 * 3 * 4     => podemos separar os primeiros numeros:
       = [1 * 2 * 3]  *  4 => preste atencao, a expressao isolada e' igual a '3!' (3! = 1 * 2 * 3) 
       = 3! * 4            => simplificando pra facilitar o nosso passo-a-passo.
  - Ou seja => n! = (n - 1)! * n, desde que n > 1.
  - Caso n == 1, n! = 1

Restricao: nao pode utilizar 'for' ou 'while'. Apenas funcoes.
"""

# Escreva aqui seu codigo
def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    assert factorial(3) == 6
    print("Parabens! 3! = 6")
    assert factorial(4) == 24
    print("Parabens! 4! = 3! * 4 = 6 * 4 = 24")
    assert factorial(0) == 1
    print("Parabens! 0! = 1")
