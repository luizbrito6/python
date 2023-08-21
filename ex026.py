from funcoes import x, leitorCoringa; 

x()


numA = leitorCoringa(int, 'Informe o primeiro número: ', 'Informe valores inteiros! Tente novamente!')
numB = leitorCoringa(int, 'Informe o segundo número: ', 'Informe valores inteiros! Tente novamente!')

if (numA > numB) :
    print(f'{numA} é maior que {numB}')

elif (numA < numB) : 
    print(f'{numB} é maior que {numA}')

else : 
    print(f'{numB} é igual a {numA}')
