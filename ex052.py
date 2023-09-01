from funcoes import x, leitorCoringa


x() 

maior = 0 
x = 0 
soma = 0 

maiorQueDezoito = 0 
menorQueCinco = 0 

while x < 10 :

    idade = leitorCoringa(int, 'Informe a idade: ', 'Informe valores válidos!')

    if idade > 18 : 
        maiorQueDezoito += 1
    
    if idade < 5 : 
        menorQueCinco += 1

    if idade > maior :
        maior = idade

    soma += idade
    x += 1

print(f'Média de idade do grupo: {soma / 10}')
print(f'Quantidade de pessoas que tem mais de 18 anos: {maiorQueDezoito}')
print(f'Quantidade de pessoas que tem menos de 5 anos: {menorQueCinco}')
print(f'Maior idade {maior}')