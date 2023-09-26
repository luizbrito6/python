from funcoes import * 

x() 

titulo('Vetor Exercício 15')

listaNome = []
listaSexo = []
listaSalario = []
for z in range(0, 5) :
    nome = leitorCoringa(str, 'Informe o nome do funcionário: ', 'Informe valores válidos!')
    listaNome.append(nome)
    x()
    menu('Qual o sexo do funcionário: ', 'Masculino', 'Feminino')
    sexo = leitorOpcoes()
    listaSexo.append(sexo)
    x()
    salario = leitorCoringa(float, 'Informe o salário do funcionário: ', 'Informe valores válidos!')
    listaSalario.append(salario)
    x()

index = 0
contadorCondicinal = 0 # Funcionárias mulheres que ganham mais de 5 mil

for nome in listaNome :

    if listaSexo[index] == 2 and listaSalario[index] > 5000 :
        if contadorCondicinal == 0 :
            print('Mulheres cadastradas que ganham mais que R$ 5000,00 \n')
                    
 
        print(f'Nome: {nome} | Sexo: Feminino | Salário: R${listaSalario[index]}')

        contadorCondicinal += 1

    index += 1


if contadorCondicinal == 0 :
    print('Não há mulheres que ganham mais de R$5000,00 cadastradas na plataforma! \n')
