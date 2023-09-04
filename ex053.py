from funcoes import leitorCoringa, x, y, titulo

# E SE NÃO TIVER HOMENS NO GRUPO - CHECK
# E SE NÃO TIVER MULHERES COM MAIS DE VINTE ANOS NO GRUPO - CHECK

x() 

titulo('EXERCÍCIO 53 - WHILE')

contador = 0 
homem = 0 
mulher = 0
somaIdade = 0
somaIdadeHomem = 0 
mulherMaiorVinte = 0

def menuSexo() : 

    while True :

        print('Informe o sexo: ')
        print('\n')
        print('(1) ------ HOMEM')
        print('(2) ------ MULHER')
        print('\n')
        sexo = leitorCoringa(int, 'Digite uma das opções: ', 'Informe valores válidos!')

        y(1)
        x()

        if sexo == 1 or sexo == 2 :
            return sexo
        else : 
            print('Escolha uma opção válida!')
    
while contador < 2 : 

    idade = leitorCoringa(int, 'Informe a idade: ', 'Informe valores inteiros!!')
    somaIdade += idade

    x() 
    sexo = menuSexo()
    if sexo == 1 : 
        homem += 1
        somaIdadeHomem += idade
    else :
        mulher += 1 
        
        if idade > 20 :
            mulherMaiorVinte += 1

    contador += 1

print(f'Número de mulheres cadastradas: {mulher}')
print('\n')
print(f'Número de homens cadastrados: {homem}')
print('\n')
print(f'Média de idade do grupo: {somaIdade / 5}')
print('\n')

if homem == 0 :
    print('Não tem homens no grupo!')
else :
    print(f'Média de idade dos homens: {somaIdadeHomem / 5}') 

print('\n')

if mulherMaiorVinte == 0 :
    print('Não tem mulhres com mais de vinte anos no grupo!')
else :
    print(F'Mulheres com mais de vinte anos: {mulherMaiorVinte}')