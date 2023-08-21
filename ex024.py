from funcoes import x, leitorCoringa

x(); 

distancia = leitorCoringa(float, 'Informe a distância em KM: ', 'Valores inválidos! Informe valores inteiros')

if distancia <= 200 : 
    valorPassagem = distancia * 0.45
else :
    valorPassagem = distancia * 0.5 

print(f'Valor da passagem: R${valorPassagem}')