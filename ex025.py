from funcoes import x, leitorCoringa

# A < B + C check
# B < A + C check
# C < A + B check
x()


segmentoA = leitorCoringa(float, 'Informe o segmento A: ', 'Valores inválidos! Informe números.')
segmentoB = leitorCoringa(float, 'Informe o segmento B: ', 'Valores inválidos! Informe números.')
segmentoC = leitorCoringa(float, 'Informe o segmento C: ', 'Valores inválidos! Informe números.')


x()


if (segmentoA > segmentoB + segmentoC) or (segmentoB > segmentoA + segmentoC) or (segmentoC > segmentoA + segmentoB) :
    print('Não é possível formar um triângulo!')

else :  
    print('É possível formar um triângulo!')
    


