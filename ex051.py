from funcoes import x, leitorCoringa

x() 

x = 0 
maior = 0
menor = 0

while x < 7 :

    valorProduto = leitorCoringa(float, 'Informe o valor do produto: ', 'Informe valores válidos!')

    if menor == 0 :
        menor = valorProduto

    if valorProduto > maior :
        maior = valorProduto
    
    if valorProduto < menor : 
        menor = valorProduto
    
    x += 1

print(f'Maior valor: R${maior}')
print(f'Menor valor: R${menor}')


