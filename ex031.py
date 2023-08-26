from funcoes import leitorCoringa, x, titulo
from random import randint




x()


# INPUTAR A OPÇÃO SENDO UM NÚMERO INTEIRO 

# TRATAR SE ESSA OPÇÃO É 1 / 2 / 3 
    # 1 - PEDRA
    # 2 - PAPEL 
    # 3 - TESOURA 

# GERAR UM NÚMERO ALEATÓRIO ENTRE 1 e 3  

# CASO POSSIVÉIS 

    # OPÇÕES IGUAL ∴ EMPATE - CHECK 
    # PEDRA (1) x PAPEL (2) ∴ PAPEL (2) CAMPEÃO - CHECK
    # PEDRA (1) x TESOURA (3) ∴ PEDRA (1) CAMPEÃO - CHECK 
    # PAPEL (2) x PEDRA (1) ∴ PAPEL (2) CAMPEÃO - CHECK
    # PAPEL (2) x TESOURA (3) ∴ TESOURA (3) CAMPEÃO - CHECK
    # TESOURA (3) x PEDRA (1) ∴ PEDRA (1) CAMPEÃO - CHECK 
    # TESOURA (3) x PAPEL (2) ∴ TESOURA (3) CAMPEÃO - CHECK    




sistema = randint(1, 3)





while True :
    titulo('JOKENPO')

    print('\n')
    print('(1) ------- PEDRA')
    print('(2) ------- PAPEL')
    print('(3) ------- TESOURA')
    print('\n')

    usuario = leitorCoringa(int, 'Informe uma das opções númericas: ', 'Digite valores inteiros')
    x()

    if usuario == 1 or usuario == 2 or usuario == 3 :
        if usuario == sistema :
            print('EMPATE!!')
        else :

            print('\n')
            x()
            
            if usuario == 1 and sistema == 2 : 
                print('PEDRA x PAPEL')
                print('\33[32mPapel campeão!\33[m')

            elif usuario == 1 and sistema == 2 : 
                print('PEDRA x TESOURA')
                print('\33[32mPedra campeão!\33[m')

            elif usuario == 2 and sistema == 1 : 
                print('PAPEL x  PEDRA')
                print('\33[32mPapel campeão!\33[m') 

            elif usuario == 2 and sistema == 3 : 
                print('PAPEL x TESOURA')
                print('\33[32mTesoura campeã!\33[m')

            elif usuario == 3 and sistema == 1 : 
                print('TESOURA x PEDRA')
                print('\33[32mPedra campeão!\33[m')

            else : 
                print('TESOURA x PAPEL')
                print('\33[32mTesoura campeã\33[m')
        break
    else : 
        print('\33[31mDigite valores entre 1 e 3!\33[m')
        print('\n')












