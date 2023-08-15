from funcoes import x;
import datetime; 



x() 
anoAtual = datetime.datetime.now().year
while True :
    try :
        anoNascimento = int(input('Informe o ano do nascimento: '))
        if  anoAtual - anoNascimento >= 18 :
            print(f'\33[32mVoçê pode votar!\33[m')
            break
        else :
            print('\33[31mVocê não pode votar!\33[m')
            break   
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')

 
