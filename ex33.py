from funcoes import leitorCoringa, x, y, titulo

# INSERÇÃO DE DADOS
    # VALOR DA CASA     
    # SALÁRIO
    # ANOS
# PROCESSAMENTO 
    # VALOR DA PRESTAÇÃO MENSAL ( VALOR DA CASA / (ANOS * 12 ))
    # SE PRESTAÇÃO MAIOR QUE (SALARIO - SALARIO * 0.3 ) - DESAPROVADO 
    # ELSE - APROVADO 


x() 

titulo('EMPRÉSTIMO BANCÁRIO')

valorImovel = leitorCoringa(float, 'Informe o valor do imóvel: ', 'Informe valores válidos!')
print('\n')
salario = leitorCoringa(float, 'Informe o salário do solicitante: ', 'Informe valores válidos!')
print('\n')
anosPagando = leitorCoringa(int, 'Informe em quantos anos será quitado o imóvel: ', 'Informe valores válidos!')

prestacao = round(valorImovel / (anosPagando * 12), 2)

msg = 'A prestação ficou no valor'

trintaPorcento = salario - (salario * 0.7)

if prestacao > trintaPorcento :
    x()
    print(f'{msg} de R${prestacao}')
    print(f'30% do sálrio: R${trintaPorcento}')
    print('\33[31mNão é possível realizar o empréstimo! Parcela superior a 30% do salário do solicitante!\33[m')

else :
    x()
    print(f'{msg} de R${prestacao}')
    print(f'30% do sálario: R${trintaPorcento}')
    print('\33[32mÉ possível realizar o empréstimo! Parcela inferior a 30% do salário do solicitante!\33[m')


