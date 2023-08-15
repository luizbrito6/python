from funcoes import x;

x() 
while True :
    try :
        salario = float(input('Informe o sálario do funcionário: '))
        print(f'\33[32mO valor do sálario com 15% de acréscimo é {salario + (salario * 0.15)}\33[m')
        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')