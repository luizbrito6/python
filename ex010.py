from funcoes import x;

x() 



while True :
    try :
        altura = float(input('Informe a altura da parede: '))
        largura = float(input('Informe a largura da parede: '))
        area = altura * largura 

        

        
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')