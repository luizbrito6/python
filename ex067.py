from funcoes import leitorCoringa, x, titulo

titulo('FOR - EX04')

fim = leitorCoringa(int, 'Informe um número para finalizar a contagem: ', 'Informe valores inteiros!')

print('\n')
for x in range(0, fim + 1) :
    print(x)
    
print('\n')