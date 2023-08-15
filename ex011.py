from funcoes import x;

x() 



while True :
    try :
        a = float(input('Informe o valor de A: '))
        b  = float(input('Informe o valor de B: '))
        c  = float(input('Informe o valor de C: '))

        print(f'O valor de ∆ é {b ** 2 - 4*a*c}')

        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')