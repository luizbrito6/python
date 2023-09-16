from funcoes import * 

x() 

idades = []
mensagem = []

for z in range(0, 3) :
    
    idade = leitorCoringa(int, 'Informe a idade: ', 'Informe valores válidos!')
    idades.append(idade)

maiorIdade = max(idades)

soma = 0
posicao = 0
posicaoMaior = []
for i in idades :
    soma += i 

    if i > 25 :
        mensagem.append(f'Idade {i} maior que 25 na posição {posicao}')

    if i == maiorIdade :
        posicaoMaior.append(posicao)
        

    posicao += 1

x() 

print(f'(A) - Média de idade: {round(soma / len(idades), 2)}') 

print('\n')
print('(B) - Idades maiores que 25 e suas posições: ')

if len(mensagem) == 0 :
        print('\33[31m    - Não cadastraram notas maiores que 25\33[m')
else :
    for m in mensagem :
        print(f'    - {m}')

print('\n')
print(f'(C) - Maior idade: {maiorIdade}')

print('\n')

print(f'(D) - Posições que a maior nota aparece: ')
for n in posicaoMaior :
    print(f'    - A maior idade aparece na posição {n}')


