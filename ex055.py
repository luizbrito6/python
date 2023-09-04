from funcoes import x, y, leitorCoringa, titulo
from random import randint

x()

numeroCerto = randint(1, 5)

contador = 0 
while contador < 4 :
    titulo('ACERTE O NÚMERO!')

    numeroUsuario = leitorCoringa(int, 'Informe um número: ', 'Digite um valor inteiro!!')

    if numeroUsuario == numeroCerto :
        print(f'\33[32mVocê acertou! Número {numeroCerto} é o correto! \33[m')
        break
    
    else : 
        contador += 1
        print('\33[31mTente novamente! Você errou o número...\33[m')
        y(1)
        x()

if  contador >= 3 :
    print('Número máximo de tentativas!!')