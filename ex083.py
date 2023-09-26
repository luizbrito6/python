from funcoes import * 
from random import randint

x() 
titulo('Vetor Exercício 13 - Desafio')

# PEGAR lstA BAGUNÇADA - CHECK
# PEGAR O MENOR NÚMERO DESSA LISTA 
# RETIRAR ESSE NÚMERO DA LISTA 
# COLOCAR ESSE NÚMERO NA LISTA ORDENADA 

lst = []
def gerarlsta() :
    for z in range(0, 30) :
        lst.append(randint(0, 99))
    
    return lst
lst = gerarlsta()


def pegarMenor(lst) :
    menor = 0
    for n in lst : 
        if n < menor or menor == 0 :
            menor = n

    return menor

menor = pegarMenor(lst) 

ordenado = []
for n in lst :
    menor = pegarMenor(lst)
    lst.remove(menor)
    ordenado.append(menor)


print(ordenado)

print('\n')





