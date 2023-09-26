from funcoes import titulo, x, leitorOpcoes, menu, leitorCoringa

x() 


titulo('FOR - EX05')

quantidadeMulher = 0 
somaPesoMulher = 0 

homemMaiorQue100 = 0 
maiorPesoHomem = 0

for z in range(0, 7) :
    

    peso = leitorCoringa(float, 'Qual o peso do usuário: ', 'Informe valores válidos!')

    x() 
    menu('Qual o sexo do usuário: ', 'MASCULINO', 'FEMININO')
    sexo = leitorOpcoes()

    if sexo == 2 :
        quantidadeMulher += 1 
        somaPesoMulher += peso
    
    if sexo == 1 and peso > 100 :
        homemMaiorQue100 += 1 

        if peso > maiorPesoHomem :
            maiorPesoHomem = peso
    
    


print('\n')
print(f'Quantidade de mulheres cadastradas: {quantidadeMulher}')
print('\n')
print(f'Homens que pesam mais de 100Kg: {homemMaiorQue100}')
print('\n')

if quantidadeMulher > 0 :
    print(f'Média de peso entre as mulheres: {somaPesoMulher / quantidadeMulher}')
    print('\n')

else :
    print('Nenhuma mulher foi cadastrada no sistema!')

print(f'Maior peso entre os homens: {maiorPesoHomem}')



