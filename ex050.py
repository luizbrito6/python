from funcoes import x 
from random import randint

x() 



x = 0 
numeros = []
maiorQueCinco = []
divisivelPorTres = []

while x < 19 : 
    numAleatorio = randint(1, 20)   
    numeros.append(numAleatorio)

    if numAleatorio > 5 :
        maiorQueCinco.append(numAleatorio)

    if numAleatorio % 3 == 0 :
        divisivelPorTres.append(numAleatorio)

    x += 1

print(f'Números sorteados: {numeros}')
print('\n')
print(f'Números maiores que cinco: {maiorQueCinco}')
print('\n')
print(f'Números divisivíveis por três: {divisivelPorTres}')