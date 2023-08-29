import os
from time import sleep


# Função para limpar o terminal 
def x() : 
    os.system('cls')


# Função que inputar um valor com o tipo primitivo específico   
def leitorCoringa(tipoPrimitivo, msg, msgError) :
        
    while True : 
        try :
            x  = tipoPrimitivo(input(f'{msg}').replace(',','.'))
        except :

            print(f'\33[31m{msgError}\33[m')

        else : 
            return x; 


# Função para fazer um título de exercício 
def titulo(titulo) :
    print('-' * 40)
    print(f'{titulo:^40}')
    print('-' * 40)
    print('\n')


# Função para dar um timer entre limpar o terminal 
def y(timer) :
    sleep(timer)



