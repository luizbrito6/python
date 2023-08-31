from funcoes import x, leitorCoringa

x() 


valorInicial = leitorCoringa(int, 'Informe o valor inicial: ', 'Informe valores inteiros!')
valorFinal = leitorCoringa(int, 'Informe o valor final: ', 'Informe valores inteiros!')
valorIncremento = leitorCoringa(int, 'Informe o valor do incremento: ', 'Informe valores inteiros!')

while valorInicial < valorFinal :

    print(valorInicial)
    valorInicial += valorIncremento