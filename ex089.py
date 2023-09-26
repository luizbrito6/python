from funcoes import * 


x() 


titulo('Funções Exercício 04')


def Gerador(msg, x, opcao) :
    

    if opcao == 1 :
        borda = '+-------=======------+'
    
    if opcao == 2 :
        borda = '~~~~~~~~:::::::~~~~~~~'

    if opcao == 3 :
        borda = '<<<<<<<<------->>>>>>>'

    print(borda)
    for z in range(0, x + 1): 
        print(f'{msg:^22}')
    print(borda)


Gerador('Primeira borda', 3, 1)
print('\n')
Gerador('Segunda borda', 3, 2)
print('\n')
Gerador('Terceira borda', 3, 3)
print('\n')