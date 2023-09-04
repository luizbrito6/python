from funcoes import x, menu, leitorOpcoes, leitorCoringa

x() 

maiorIdade = 0
menorIdade = 0

contadorHomens = 0
somaIdadeHomens = 0
while True : 

    menu('Informe o sexo: ', 'MASCULINO', 'FEMININO')
    sexo = leitorOpcoes()

    x()

    idade = leitorCoringa(int, 'Informe a idade: ', 'Informe valores inteiros!')

    if sexo == 1 :
        contadorHomens += 1
        somaIdadeHomens += idade

    if sexo == 2 :

        if menorIdade == 0 :
            menorIdade = idade
    
        if idade < menorIdade :
            menorIdade = idade


    if idade > maiorIdade :
        maiorIdade = idade

    x()
    menu('Deseja continuar?', 'SIM', 'NÃO')
    opcao = leitorOpcoes()

    x()

    if opcao == 2 :
        break


print(f'Maior idade: {maiorIdade}')
print('\n')
print(f'Quantidade de homens cadastrados: {contadorHomens}')
print('\n')
print(f'Idade da mulher mais jovem cadastrada: {menorIdade}')
print('\n')
print(f'Idade média dos homens cadastrados {somaIdadeHomens // contadorHomens }')