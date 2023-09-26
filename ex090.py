from funcoes import *

x() 
titulo('Funções Exercício 05')
def Somador() :
    z = leitorCoringa(float, 'Informe o primeiro valor: ', 'Digite valores válidos!')
    y = leitorCoringa(float, 'Informe o segundo valor: ', 'Digite valores válidos!')
    return z + y

print(f'Resultado: {Somador()}')