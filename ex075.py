from funcoes import *

x() 

titulo('Vetor Exercício 05')

elementos = [1, 1]


for x in range (0, 14) :
    
    fibonacci = elementos[-2] + elementos[-1]

    elementos.append(fibonacci)

print(elementos)