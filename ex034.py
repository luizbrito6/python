from funcoes import leitorCoringa, x, y, titulo

x() 

titulo('Índice de Massa Corpórea - IMC')

peso = leitorCoringa(float, 'Informe o peso: ', 'Informe valores válidos!')
altura = leitorCoringa(float, 'Informe a altura: ', 'Informe valores válidos!')

imc = peso / altura ** 2 

print(imc)


if imc > 40 :
    print('Obseidade mórbida')

elif  imc >= 30 and imc <= 40 :
    print('Obesidade')
    
elif imc > 25 and imc < 30 :
    print('Sobrepeso')

elif 18.5 > imc <= 25 :
    print('Peso ideal')

else : 
    print('Abaixo do peso')