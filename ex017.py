from funcoes import x;

x() 
while True :
    try :
        velocidade = int(input('Informe a velocidade: '))

        if velocidade > 80 :
            print(f'\33[31mVocê foi mutado! E o valor da multa foi de R${(velocidade - 80) * 5}\33[m')
            break
        else :
            print('\33[32mVocê não foi mutado!\33[m')
            break   
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

 
