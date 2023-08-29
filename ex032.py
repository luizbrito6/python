from funcoes import x, y, leitorCoringa, titulo
from random import randint


x()


titulo('ACERTE O NÚMERO!')

numeroCerto = randint(1, 5)


while True :

    numeroUsuario = leitorCoringa(int, 'Informe um número: ', 'Digite um valor inteiro!!')

    if numeroUsuario == numeroCerto :
        print(f'\33[32mVocê acertou! Número {numeroCerto} é o correto! \33[m')
        break
    
    else : 
        print('\33[31mTente novamente! Você errou o número...\33[m')

        y(2)
        x()
