from funcoes import leitorCoringa, x, titulo

titulo('FOR - EX03')

num = leitorCoringa(int, 'Informe um número para calcular a tabuada: ', 'Informe valores inteiros!')

print('\n')
for x in range(1, 11) :
    print(f'{num} x {x} = {num * x}')
    
print('\n')