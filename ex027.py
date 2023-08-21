from funcoes import x, leitorCoringa; 


x();


notaA = leitorCoringa(float, 'Informe a primeira nota: ', 'Notas inválidas! Tente novamente ... ')
notaB = leitorCoringa(float, 'Informe a segunda nota: ', 'Notas inválidas! Tente novamente ... ')

media = (notaA + notaB) / 2

if media <= 4.9 :
    print(f'\33[31m{round(media, 1)}: REPROVADO\33[m')
elif media >= 5 and media <= 6.9 :
    print(f'\33[33m{round(media, 1)}: RECUPERAÇÃO\33[m')
else :
    print(f'\33[32m {round(media, 1)}: APROVADO\33[m')




