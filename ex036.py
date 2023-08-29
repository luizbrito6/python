from funcoes import x, y, leitorCoringa, titulo

x() 
titulo('Programa de vida saudável')
hora = leitorCoringa(int, 'Quantas horas de atividade uma pessoa teve por mês? ', 'Informe valores válidos!')

if hora <= 10 : 
    ponto = 2 * hora

elif hora > 10 and hora <= 20 : 
    ponto = 5 * hora

else :
    ponto = 10 * hora

print(f'Valor ganho em dinheiro: R${round(ponto * 0.05, 2)}')