from funcoes import * 

x() 

titulo('Vetor Exercício 07')

nomes = []

for z in range(0, 7): 
    
    nome = leitorCoringa(str, 'Informe o nome: ', 'Informe valores válidos!')
    nomes.append(nome)

x() 

while z > -1: 

    print(nomes[z])
    z -= 1