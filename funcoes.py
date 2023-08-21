import os 

def x() : 
    os.system('cls')


def leitorCoringa(tipoPrimitivo, msg, msgError) :
        
    while True : 
        try :
            x  = tipoPrimitivo(input(f'{msg}').replace(',','.'))
        except :

            print(f'\33[31m{msgError}\33[m')

        else : 
            return x; 


