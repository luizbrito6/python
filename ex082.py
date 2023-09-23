from funcoes import * 

x() 

titulo('Vetor Exercício 12')

soma = 0
notas = []
maiorQueMedia = []
posicoesMaiorNota = []

for n in range(0, 5) :

    nota = leitorCoringa(float, 'Informe a nota: ', 'Informe valores válidos!')
    notas.append(nota)

    soma += nota

x() 

media = soma / len(notas)
maiorNota = max(notas)

posicao = 0
for nota in notas :
    if nota > media :
        maiorQueMedia.append(nota)
    
    if nota == maiorNota :
        posicoesMaiorNota.append(posicao)
    

    posicao += 1

print(f'Média da turma: {media}')
print(f'Quantidade de notas acima da média: {len(maiorQueMedia)}')
print(f'Notas maiores que a média: {maiorQueMedia}')
print(f'Maior nota digitada: {maiorNota}')
print(f'Posições que a maior nota aparece: {posicoesMaiorNota}')

