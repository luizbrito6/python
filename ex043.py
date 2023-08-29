from funcoes import leitorCoringa, x

x() 


num = leitorCoringa(int, 'Informe um número inteiro:', 'Informe valores inteiros!')

while num > 0 :
    print(num)
    num -= 1
    
print('Acabou!')      