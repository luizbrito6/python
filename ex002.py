from funcoes import x;
x()


try :
    nome = input(str('Qual o seu nome? '))
    print('\n')
    print(f'Olá {nome}, é um prazer te conhecer!')

except :
    print('\33[31mOcorreu um erro!\33[m')
