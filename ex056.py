from funcoes import leitorCoringa, x

x() 

soma = 0 

while True :
    num = leitorCoringa(float, 'Informe um número: ', 'Informe números!!!')  

    if num == 1111 :
        break  

    soma += num

print(f'Soma: {soma}')