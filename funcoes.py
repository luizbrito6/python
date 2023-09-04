import os
from time import sleep



# Função para limpar o terminal 
def x() : 
    return os.system('cls')


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



# Função para ler duas opções 
def leitorOpcoes() :

    while True :
        
        opcao = leitorCoringa(int, 'Informe uma das opções: ', 'Informe valores inteiros!')

        if opcao == 1 or opcao == 2 :
            return opcao
        else : 
            print('\33[31mInforme 1 ou 2 ...\33[m')


# Função para fazer um menu com duas opções 

def menu(pergunta, opcaoA, opcaoB) : 

    print(f'{pergunta}')
    print('\n')
    print(f'(1) ------- {opcaoA} ')
    print(f'(2) -------  {opcaoB}')
    print('\n')



