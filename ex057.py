from funcoes import leitorOpcoes, leitorCoringa, x, menu

x()

somaSalarioHomem = 0
somaSalarioMulher = 0



while  True :

    salario = leitorCoringa(float, 'Informe o salário do funcionário: ', 'Informe valores válidos!')

    x()

    menu('Informe o sexo: ', 'MASCULINO', 'FEMININO')
    sexo = leitorOpcoes()

    if sexo == 1 :
        somaSalarioHomem += salario
    else :
        somaSalarioMulher += salario

    x()

    menu('Deseja continuar: ', 'SIM', 'NÃO')
    
    controlador = leitorOpcoes()

    x() 

    if controlador == 2 :
        print('Obrigado por usar nosso sistema!')

        break

    x()



if somaSalarioHomem > 0 :
    print('\n')
    print(f'Total de salários para homens: R${somaSalarioHomem}')
else :
    print('\n')
    print('Nenhum homem foi inserido no sistema...')

if somaSalarioMulher > 0 :
    print('\n')
    print(f'Total de salários para mulheres: R${somaSalarioMulher}')
else :
    print('\n')
    print('Nenhuma mulher foi inserida no sistema...')

