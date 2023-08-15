from funcoes import x;

x()


while True :
    try :
        nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
        nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))

        media = (nota1 + nota2) / 2


        if media > 7 :
            print('\33[32mO aluno teve bom desempenho!\33[m')
        else :
            print('\33[31mO aluno não obteve um bom desempenho!\33[m')
        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')
