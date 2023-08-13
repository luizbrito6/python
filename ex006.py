from funcoes import x;

x()


while True :
    try :
        num = int(input('Digite um número: '))
        
        x()
        print('\n')
        print(f'Antecessor de {num} é {num - 1}')
        print(f'Sucessor de {num} é {num + 1}')
        print('\n')

        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')