from funcoes import *


# 9 (8-7-6-5-4-3-2-) 1
# 
x() 
titulo('Funções Exercício 13')


def SuperSomador(inicio, fim) :
    soma = 0
    
    for z in range(inicio, fim + 1) :
        soma += z
    
    return soma

   
print(SuperSomador(15, 19))