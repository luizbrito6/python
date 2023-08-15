from funcoes import x;

x() 



while True :
    try :
        altura = float(input('Informe a altura da parede: ').replace(',', '.'))
        largura = float(input('Informe a largura da parede: ').replace(',', '.'))
        area = int(altura * largura) 

        print(f'A área da parede é {area}m² e a quantidade de tinta necessaria {area // 2} litros.')
        
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')