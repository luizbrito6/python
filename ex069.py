from funcoes import leitorCoringa, x 


x() 


razao = leitorCoringa(float, 'Informe a razão da PA: ', 'Informe valores válidos!')
primeiroTermo = leitorCoringa(float, 'Informe o primeiro termo da PA: ', 'Informe valores válidos!')


termos = []

for n in range(1, 11) :
    termo = primeiroTermo + (n - 1) * razao 
    termos.append(termo)


somaTermo = (termos[0] + termos[9]) * n / 2 

print('\n')
print(f'Termos: {termos}')
print('\n')
print(f'Soma dos termos: {somaTermo}')
print('\n')


