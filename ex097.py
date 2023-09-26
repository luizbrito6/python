#  A > B e B > C ∴ A > C
#  B > A e A > C ∴ B > C
#  C > B e B > A ∴ C > A



from funcoes import *

x() 

titulo('Funções Exercício 12')



def Maior(a, b, c) :

    if a > b and b > c: 
        print(f'{a} é o maior número!')
    elif b > a and a > c : 
        print(f'{b} é o maior número!')

    elif a == b == c : 
        print('Os três números são iguais!')
    else :
        print(f'{c} é o maior número!')

print('\n')

Maior(9,8,7)
