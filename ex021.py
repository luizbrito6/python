from funcoes import x;

x()

while True :
    try :
        ano = int(input('Informe o ano: '))
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

    else : 
        if ano % 4 == 0 :
            print('\33[32mO ano é bissexto!\33[m')
        else :
            print('\33[32mO ano não é bissexto!\33[m')
        break
