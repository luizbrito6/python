from funcoes import x;
import datetime; 


anoAtual = datetime.datetime.now().year

x()

while True :
    
    try :
        ano = int(input('Informe o ano de nascimento: '))
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

    else : 

        idade = anoAtual - ano

        if idade < 18 :
            print(f'\33[32mFaltam {18 - idade} ano(s) para o alistamento!\33[m')

        elif idade == 18  : 
            print(f'\33[32mSeu alistamento é no ano atual: {anoAtual}\33[m')
            
        else :
            print(f'\33[32mSe passaram {idade - 18} ano(s) para o alistamento!\33[m')
        break
