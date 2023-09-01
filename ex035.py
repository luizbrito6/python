from funcoes import x, y, leitorCoringa, titulo


# TIPOS DE CARRO
    # Carro de luxo ⟾ 150 reais
    # Carro popular ⟾ 90 reais

x()

titulo('Aluguel de carros')

while True : 

    print('\n')
    print('(1) ------- CARRO POPULAR')
    print('(2) ------- CARRO DE LUXO')
    print('\n')
    
    carro = leitorCoringa(int, 'Informe o tipo do carro: ', 'Informe valores inteiros válidos!')
    x()

    if carro == 1 or carro == 2 :
        break
    else :
        x()
        print('\33[31mDigite 1 ou 2 ...\33[m')
    

dias = leitorCoringa(int, 'Informe os dias alugados: ', 'Informe valores inteiros válidos!')
x()
km = leitorCoringa(int, 'Informe quantos Km foram percorridos: ', 'Informe valores válidos!') 

if carro == 1 :

    if km <= 100 :
        valorFinal = dias * 90 + (km * 0.2)
    else : 
        valorFinal = dias * 90 + (km * 0.1)

else : 
    
    if km < 200 :
        valorFinal = dias * 150 + (km * 0.3)
    else : 
        valorFinal = dias * 150 + (km * 0.25)
        

print(f'Valor do aluguel: R${round(valorFinal, 2)}')