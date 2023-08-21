from funcoes import x, leitorCoringa

x() 

nome = leitorCoringa(str, 'Informe o nome do funcionário: ', 'Valor inválido! Tente novamente...')
salario = leitorCoringa(float, 'Informe o salário do funcionário: ', 'Salário inválido! Tente novamente...')
anosEmpresa = leitorCoringa(int, 'Informe a quantos anos o funcionário está na empresa: ', 'Valor inválido! Tente novamente...')

x() 

if anosEmpresa <= 3 :
    print(f'{nome} | Salário com aumento de 3%: R${int(salario + (salario * 0.03))},00')
elif anosEmpresa > 3 and anosEmpresa < 10 :
    print(f'{nome} | Salário com aumento de 12,5%: R${int(salario + (salario * 0.125))},00')
else :
    print(f'{nome} | Salário com aumento de 20%: R${int(salario + (salario * 0.20))},00')

