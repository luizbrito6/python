from funcoes import x, y, leitorCoringa, titulo


x()

titulo('REAJUSTE SALARIAL')

salarioAtual = leitorCoringa(float, 'Informe o salário atual do funcionário: ', 'Informe valores válidos!')
x()
ano = leitorCoringa(float, 'Informe quantos anos de empresa: ', 'Informe valores válidos!')
x()


while True :

    print('\n')
    print('(1) ------- FEMININO')
    print('(2) ------- MASCULINO')
    print('\n')
    genero = leitorCoringa(int, 'Informe o gênero do funcionário: ', 'Informe valores válidos!')

    x()


    if genero == 1 or genero == 2 :
        break

    else :
        x()
        y(1)
        print('\33[31mDigite 1 ou 2 ...\33[m')


if genero == 1 : 

    if ano < 15 :
        salarioReajustado = salarioAtual + (salarioAtual * 0.05)
    
    elif ano >= 15 and ano <= 20 :
        salarioReajustado = salarioAtual + (salarioAtual * 0.12)

    else :
        salarioReajustado = salarioAtual + (salarioAtual * 0.23)

else : 
    if ano < 20 :
        salarioReajustado = salarioAtual + (salarioAtual * 0.03)
    
    elif ano >= 20 and ano < 30 :
        salarioReajustado = salarioAtual + (salarioAtual * 0.13)

    else : 
        salarioReajustado = salarioAtual + (salarioAtual * 0.25)


print(f'Salário reajustado: R${salarioReajustado}')