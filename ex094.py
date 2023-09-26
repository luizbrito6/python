from funcoes import * 

x()

titulo('Funções Exercício 09 - Desafio')

def Fibonacci(fim) :
    elementos = [1, 1]
    for x in range (0, fim - 2) :
        fibonacci = elementos[-2] + elementos[-1]
        elementos.append(fibonacci)

    print(elementos)

Fibonacci(5)
Fibonacci(9)