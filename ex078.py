from funcoes import * 

x() 

titulo('Vetor Exercício 08')

numeros = []
multiplos = []
posicoes = []

for z in range(0, 14): 
    
    num = leitorCoringa(int, 'Informe o número: ', 'Informe valores válidos!')
    numeros.append(num)

    if num % 10 == 0 :
        multiplos.append(num)
        posicoes.append(z)

x() 

y = 0

if len(multiplos) == 0 :
    print('\n')
    print('\33[31mNão foram lidos múltiplos de 10...\33[m')
    print('\n')

else :

    print('\n')

    for multiplo in multiplos :
        print(f'Número múltiplo: {multiplo} na posição: {posicoes[y]}')
        y += 1
    
    print('\n')

    

