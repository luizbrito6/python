from funcoes import leitorCoringa, x, menu, leitorOpcoes

x() 

somaNumero = 0 
menorNumero = 0

contadorNumero = 0
numeroPar = 0 

while True :

    num = leitorCoringa(float, 'Informe um número: ', 'Informe valores inteiros!')
    
    somaNumero += num
    contadorNumero += 1

    if menorNumero == 0 :
        menorNumero = num
    
    if num < menorNumero :
        menorNumero = num

    if num % 2 == 0 : 
        numeroPar += 2

    x()
    menu('Deseja continuar?', 'SIM', 'NÃO')
    opcao = leitorOpcoes()
    x()

    if opcao == 2 :
        break

print('\n')
print(f'Somatório números: {somaNumero}')
print('\n')
print(f'Menor número: {menorNumero}')
print('\n')
print(f'Média: {somaNumero / contadorNumero}')
print('\n')
print(f'Quantidade de números pares: {numeroPar}')
print('\n')
