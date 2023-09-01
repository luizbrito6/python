from funcoes import leitorCoringa


soma  = 0 ;
x = 0; 

while x < 7 :
    num = leitorCoringa(int, 'Informe o número:  ', 'Informe valores inteiros!')
    soma += num
    x += 1

print(f'Soma: {soma}')