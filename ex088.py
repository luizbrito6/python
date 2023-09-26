from funcoes import * 


x() 


titulo('Funções Exercício 03')


def Gerador(msg, x) :
    
    print('+-------=======------+ ')
    for z in range(0, x + 1): 
        print(f'{msg:^22}')
    print('+-------=======------+ \n')


Gerador('For + Def', 5)