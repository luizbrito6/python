from funcoes import x;

x()


while True :
    try :
        num = float(input('Digite um número: ').replace(',', '.'))
        
        x()
        print('\n')
        print(f'Dobro de {num} é {num * 2}')
        print(f'Terça parte de {num} é {round(num / 3, 5)}')
        print('\n')

        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')