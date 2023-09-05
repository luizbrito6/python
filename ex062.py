from funcoes import leitorCoringa, x, menu, leitorOpcoes

x() 

contadorIdade = 0 
somaIdade = 0 
contadorMais21 = 0

while True :

    idade = leitorCoringa(int, 'Informe a idade do usuário: ', 'Informe valores inteiros!')
    contadorIdade += 1 
    somaIdade += idade

    if idade >= 21 :
        contadorMais21 += 1
    x() 

    menu('Deseja continuar?', 'SIM', 'NÃO')
    opcao = leitorOpcoes()
    x()

    if opcao == 2 :
        break

print(f'Quantidade de idades digitadas: {contadorIdade}')
print('\n')
print(f'Média de idade entre os participantes: {somaIdade / contadorIdade}')
print('\n')
print(f'Quantidade de pessoas com 21 anos ou mais: {contadorMais21}')
print('\n')