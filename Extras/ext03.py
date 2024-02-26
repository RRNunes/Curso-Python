"""
Faca um programa que retorne o n-esimo numero na sequencia de fibonnaci.
Suponha que a sequencia comece com n = 0, onde fibonnaci(0) = 0.

A sequencia de fibonnaci eh quando um número equivale à soma dos dois
números que vieram antes dele, por isso precisamos definir os dois primeiros:

fibonacci(0) = 0
fibonacci(1) = 1

Onde temos que:

fibonacci(2) = fibonnaci(0) + fibonnaci(1) = 0 + 1 = 1
fibonacci(3) = fibonnaci(1) + fibonnaci(2) = 1 + 1 = 2

Seguindo a sequencia:

0, 1, 1, 2, 3, 5, 8, ...

Restricao: nao pode utilizar 'for' ou 'while'. Apenas funcoes.
"""

# Escreva aqui seu codigo
def fibonacci(n: int):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    assert fibonacci(0) == 0
    print("Parabens! Fibonacci #0 = 0")
    assert fibonacci(4) == 3
    print("Parabens! Fibonacci #4 = 3")
    assert fibonacci(10) == 55
    print("Parabens! Fibonacci #10 = 55")
