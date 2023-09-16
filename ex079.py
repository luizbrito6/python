from funcoes import * 

x() 

titulo('Vetor Exercício 08')


numeros = []
for z in range(0, 10):  
    num = leitorCoringa(int, 'Informe o número: ', 'Informe valores válidos!')

    numeros.append(num)


x() 

z = 0

for n in numeros :

    if n % 2 == 0 :
        print(f'{n} é par - Posição {z}')
    
    z += 1
    
        