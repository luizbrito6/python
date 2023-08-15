from funcoes import x;

x() 



while True :
    try :
        valorProduto = float(input('Informe o valor do produto: '))

        print(f'\33[32mO valor do produto com 5% de desconto é {valorProduto - (valorProduto * 0.05)}\33[m')
    

        break 
    except :
        print('\33[31mInforme valores válidos! Tente novamente.\33[m')