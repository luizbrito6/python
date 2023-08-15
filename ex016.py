from funcoes import x;

x() 
while True :
    try :
        cigarro = int(input('Número de cigarros por dia: '))
        ano = int(input('Quantos anos fumando: '))

        tempoPerdido = cigarro * (ano * 365) * 10 / 60 / 24 


        print(f'{round(tempoPerdido, 0)} dias foram perdidos') 
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

 
