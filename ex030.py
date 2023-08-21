from funcoes import x, leitorCoringa

# TODOS IGUAIS 
    # A = B e B = C ∴ C = A 
# DOIS IGUAIS
    # A = B e B != C ∴ A != C
    # B = C e B != A ∴ C != A
    # A = C e C != B ∴ A != B 
    
# TODOS DIFERENTES 
    # else 


x()



segmentoA = leitorCoringa(float, 'Informe o segmento A: ', 'Valores inválidos! Informe números.')
segmentoB = leitorCoringa(float, 'Informe o segmento B: ', 'Valores inválidos! Informe números.')
segmentoC = leitorCoringa(float, 'Informe o segmento C: ', 'Valores inválidos! Informe números.')


x()


if (segmentoA > segmentoB + segmentoC) or (segmentoB > segmentoA + segmentoC) or (segmentoC > segmentoA + segmentoB) :
    print('Não é possível formar um triângulo!')

else :  
    print('É possível formar um triângulo!')

    if segmentoA == segmentoB and segmentoB == segmentoC :
        print('EQUILÁTERO: Todos os lados são iguais!')

    elif (
            (segmentoA == segmentoB and segmentoB != segmentoC) or
            (segmentoB == segmentoC and segmentoB != segmentoA) or 
            (segmentoA == segmentoC and segmentoC != segmentoB)
        ):
        print('ISÓSCELES: Dois lados são iguais!')

        
    else :
        print('ESCALENO: Todos os lados são diferentes!')


    
    


