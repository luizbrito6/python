from funcoes import x;

x() 
while True :
    try :

        dia = int(input('Informe o número de dias: ').replace(',', '.'))
        km = int(input('Informe o número de KM: ').replace(',', '.'))

        print(f'\33[32mTotal a pagar: R${dia * 90 + km * 0.2}\33[m')
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')