from funcoes import x;

x() 



while True :
    try :
        
        money = float(input('Informe seu valor em carteira: ').replace(',', '.'))

        if money < 3.45 : 
            print('\33[32mVocê não pode comprar nenhum dolar!\33[m')
            break

        print('\n') 

        print(f'Valor em dolares que você pode comprar: US$ {round(money / 3.45, 2)}')


        break
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')