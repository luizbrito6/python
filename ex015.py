from funcoes import x;

x() 
while True :
    try :
        diasTrabalhados = int(input('Informe os dias trabalhados: '))

        print(f'Salário: R${8 * 25 * diasTrabalhados}')
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')