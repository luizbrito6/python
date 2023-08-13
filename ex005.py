from funcoes import x;

x()


while True :
    try :
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))

        print(f'A média entre {nota1} e {nota2} é igual a {(nota1 + nota2) / 2}')

        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')
