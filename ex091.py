from funcoes import *

x() 

titulo('Funções Exercício 06')

numA = leitorCoringa(float, 'Informe o primeiro valor: ', 'Informe valores válidos!')
x()
numB = leitorCoringa(float, 'Informe o segundo valor: ', 'Informe valores válidos!')

def Maior(a, b) :

    if a > b : 
        print(f'{a} é o maior número!')
    elif a == b : 
        print('Os número são iguais!')
    else :
        print(f'{b} é o maior número!')

print('\n')
Maior(numA, numB)