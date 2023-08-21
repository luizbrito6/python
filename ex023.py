from funcoes import x;
import datetime; 



x()

while True :
    
    try :
        nome = str(input('Informe seu nome: '))
        valor = float(input('Informe o valor da compra: '))

        x() 

        
        print('Informe seu sexo:')
        print('(1) - Masculino')
        print('(2) - Feminino')
        print('\n')
        sexo = int(input('Escolha uma das opções: '))

        if sexo != 1 and sexo !=2 :
            print('Informe valores válidos! Tente novamente.')
            break 
        
        

        x()

    except :
        x()
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

    else : 
        
        if sexo == 1 :
            print(f'{nome} seu desconto foi de: R${valor * 0.05}')
            print('\n')
            print(f'valor da compra pós desconto: R${valor - valor * 0.05}')
        
        else :
            print(f'Seu desconto foi de: R${valor * 0.13}')
            print('\n')
            print(f'valor da compra pós desconto: R${valor - valor * 0.13}')
        break
