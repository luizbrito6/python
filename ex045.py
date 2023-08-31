from funcoes import leitorCoringa, x

x()

while True :

    valorInicial = leitorCoringa(int, 'Informe o valor inicial: ', 'Informe valores inteiros!')
    valorFinal = leitorCoringa(int, 'Informe o valor final: ', 'Informe valores inteiros!')


    if valorInicial > valorFinal :
        print('O valor inicial tem que ser menor que o final!')

    else :
        valorIncremento = leitorCoringa(int, 'Informe o valor do incremento: ', 'Informe valores inteiros!')
        break



while valorInicial < valorFinal :
    
    print(valorInicial)
    valorInicial += valorIncremento