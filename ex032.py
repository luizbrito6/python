from funcoes import x, leitorCoringa, titulo;
from random import randint


x()


titulo('ACERTE O NÚMERO!')

numeroCerto = randint(1, 5)





    
while True :

    numeroUsuario = leitorCoringa(int, 'Informe um número: ', 'Digite um valor inteiro!!')


    if numeroUsuario == numeroCerto :
        print(f'Você acertou o número! {numeroCerto}')
        break
    
    else : 
        print('Tente novamente! Você errou o número...')
