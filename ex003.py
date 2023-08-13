from funcoes import x

x()


while True : 

    nomeFuncionario = input('Qual o seu nome? ')

    try :
        salario = float(input('Qual o seu salário? '))
        print('\n')
        print(f'Olá {nomeFuncionario}, seu salário é R${salario} em Junho')
        print('\n')


        break 
    except: 
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')