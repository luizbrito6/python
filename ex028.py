from funcoes import x, leitorCoringa 

x()

altura = leitorCoringa(float, 'Informe a altura do terreno: ', 'Altura inválida! Tente novamente...')
largura = leitorCoringa(float, 'Informe a largura do terreno: ', 'Largura inválida! Tente novamente...')
area = altura * largura


if area < 100 :
    print(f'{int(area)}m² | Terreno popular')
elif area >= 100 and area <= 500:
    print(f'{int(area)}m² | Terreno master')
else :
    print(f'{int(area)}m² | Terreno VIP')