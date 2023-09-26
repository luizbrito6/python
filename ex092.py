from funcoes import *

x() 
titulo('Funções Exercício 07')

num = leitorCoringa(int, 'Informe um número: ', 'Informe valores válidos!')
def ParOuImpar(num) :
    return  print('Par' if num % 2 == 0 else 'Ímpar')

ParOuImpar(num)