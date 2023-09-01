from funcoes import leitorCoringa, x

x(); 

x = 0
par = 0 
impar = 0

while x < 6 :

    num = leitorCoringa(int, 'Informe o número:  ', 'Informe valores inteiros!')

    if num % 2 == 0 :
        par += 1

    else :
        impar += 1
    
    x += 1


print(f'Quantidade de números pares: {par}')
print(f'Quantidade de números ímpares: {impar}')


