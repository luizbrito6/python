from funcoes import x, y, leitorCoringa

# CONDIÇÃO A = 

x() 

contador = 0 
somaAltura = 0
maisQueNoventa = 0 
condicaoA = 0 # Pessoas que pesam menos de 50Kg tem menos de 1.60m
condicaoB = 0 # Pessoas que medem mais de 1.90m pesam mais de 100Kg
while contador < 2 :

    altura = leitorCoringa(float, 'Informe a altura: ', 'Informe valores válidos!')
    somaAltura += altura
    peso = leitorCoringa(float, 'Informe o peso: ', 'Informe valores válidos!')

    print(contador)

    if peso > 90 : 
        maisQueNoventa += 1
    
    if peso < 50 and altura < 1.6 :
        condicaoA += 1
    
    if altura > 1.9 and peso > 100 :
        condicaoB += 1
  
  
    x() 
    contador += 1 

print(f'Média de altura do grupo: {somaAltura / 2}')
print('\n')
print(f'Pessoas que pesam mais de 90Kg: {maisQueNoventa}')
print('\n')
print(f'Pessoas que pesam menos de 50Kg tem menos de 1.60m: {condicaoA}')
print('\n')
print(f'Pessoas que medem mais de 1.90m pesam mais de 100Kg: {condicaoB}')
