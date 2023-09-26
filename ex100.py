from funcoes import * 

x() 

def Media(n1, n2) :
    return (n1 + n2) / 2

media = Media(7, 5)


def Situacao(media) : 

    if media >= 7 :
        msg = 'Aprovado!'
    
    elif media >= 5 and media < 7 : 
        msg ='Recuperação!'

    else : 
        msg = 'Reprovado!'

    return msg

print(Situacao(media))
