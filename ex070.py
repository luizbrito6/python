from funcoes import *

x() 

titulo('Sequência de Fibonacci')

elementos = [1, 1]

print(elementos[0])
print(elementos[1])

for x in range (0, 8) :
    
    fibonacci = elementos[-2] + elementos[-1]

    print(fibonacci)
    elementos.append(fibonacci)

    