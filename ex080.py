from funcoes import * 
from random import randint

x() 
titulo('Vetor Exercício 10')
numeros = []

for z in range (0, 30) :
    numeros.append(randint(1, 15)) 


key = leitorCoringa(int, 'Informe a chave de pesquisa: ', 'Informe valores válidos!')

p = 0
contador = 0

for n in numeros :

    if key == n :
        print('\n')
        print(f'Chave {key} encontrada na posição {p}')
        contador += 1 
    
    p += 1

print('\n')
if contador == 0 :
    print(f'\33[31mA chave {key} não foi encontrada!\33[m')







