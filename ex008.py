from funcoes import x;

x()


while True :
    try :
        
        distancia = float(input('Qual a distância percorrida em metros? ').replace(',', '.'))

        print('\n')
        print(f'{distancia / 1000} KM')
        print(f'{distancia / 100} HM')
        print(f'{distancia / 10} DAM')
        print(f'{distancia * 10} DM')
        print(f'{distancia * 100} CM')
        print(f'{distancia * 1000} MM')
        print('\n')

        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')