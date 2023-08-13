from funcoes import x

x()

while True :
    try :
        valorA = int(input('Digite o primeiro valor: '))
        valorB = int(input('Digite o segundo valor: '))

        print(f'A soma entre {valorA} e {valorB} é igual a {valorA + valorB}.')

        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

