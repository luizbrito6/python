from funcoes import * 

# FUNÇÃO VERIFICA O PRIMEIRO 

x()

titulo('Vetor Exercício 14')
listaNome = []
listaIdade = []


for z in range(0, 9) : 
    nome = leitorCoringa(str, 'Informe o nome: ', 'Informe um nome válido!')
    idade = leitorCoringa(int,  'Informe a idade: ', 'Informe valores inteiros válidos!')

    listaNome.append(nome)
    listaIdade.append(idade)

    x()

x()

contador = 0 
contadorIdadeMenor = 0

contadorCondicinal = 0 # Funcionárias mulheres que ganham mais de R$5 mil
for idade in listaIdade : 

    if idade < 19 :
        if contadorIdadeMenor == 0 :
            print('Pessoas cadastradas menores de idade: ')

        ternario = idade if (idade > 9) else  '0' + str(idade)   
        print(f'{listaNome[contador]} | {ternario} anos')
        contadorIdadeMenor += 1

    contador += 1   