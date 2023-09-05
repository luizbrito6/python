from funcoes import menu, x, leitorOpcoes, leitorCoringa

x()

nomeMulherMaisVelha = ''
nomeMulherMaisJovem = ''

menorIdade = 0 
maiorIdade = 0

somaIdade = 0
contadorUsuario = 0
contadorMulher = 0 

homemMaisTrinta = 0
mulherMenosDezoito = 0
while True : 

    nome = leitorCoringa(str, 'Informe o nome: ', 'Informe valores válidos!')
    x()

    idade = leitorCoringa(int, 'Informe a idade: ', 'Informe valores inteiros!')
    somaIdade += idade
    x() 

    menu('Informe o sexo: ', 'MASCULINO', 'FEMININO')
    sexo = leitorOpcoes()
    x()

    menu('Deseja continuar?', 'SIM', 'NÃO')
    opcao = leitorOpcoes()
    x()

    if sexo == 1 and idade > 30 :
        homemMaisTrinta += 1


    if sexo == 2 :

        contadorMulher += 1

        if menorIdade == 0 :
            menorIdade = idade
            nomeMulherMaisJovem = nome
        
        if idade < menorIdade :
            menorIdade = idade
            nomeMulherMaisJovem = nome
            
        if idade > maiorIdade :
            maiorIdade = idade
            nomeMulherMaisVelha = nome

        if idade < 18 :
            mulherMenosDezoito += 1
            


    contadorUsuario += 1

    if opcao == 2 :
        break


if contadorMulher > 0 : 
    print('\n')
    print(f'Nome da mulher mais jovem: {nomeMulherMaisJovem} | Idade: {menorIdade} anos')
    print('\n')
    print(f'Nome da mulher mais velha: {nomeMulherMaisVelha} | Idade: {maiorIdade} anos')
else : 
    print('Nenhuma mulher foi cadastrada no programa!')
print('\n')
print(f'Média de idade dos usuários cadastrados: {somaIdade / contadorUsuario} anos')
print('\n')
print(f'Quantidade de homens com mais de trinta anos: {homemMaisTrinta}')
print('\n')
print(f'Quantidade de mulheres com menos de dezoito anos: {mulherMenosDezoito}')
print('\n')