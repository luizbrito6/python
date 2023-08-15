from funcoes import x;

x()


while True :
    try :
        num = float(input('Informe um número: ').replace(',', '.'))
        
        if num % 2 == 0:
            print('\33[32mO número é par\33[m')
        else :
            print('\33[31mO número é ímpar\33[m')
        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')
