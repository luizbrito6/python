from funcoes import x, leitorCoringa

x() 


idade = 0
contadorAlunos = 0
somaIdades =  0
while True :

    idade = leitorCoringa(int, 'Informe a idade do aluno: ', 'Informe valores inteiros!')

    if idade == 999 :
        break

    somaIdades += idade

    contadorAlunos += 1

x()

print(f'Número de alunos na classe: {contadorAlunos}')
print(f'Média das idades dos alunos: {somaIdades // contadorAlunos}')
print('\n')