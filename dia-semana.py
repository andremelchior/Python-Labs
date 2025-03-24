n = 0
while n <= 7:
    s = int(input('Semana? '))
    if s == 1:
        print('Domingo')
    elif s == 2:
        print('Segunda-Feira')
    elif s == 3:
        print('Terça-Feira')
    elif s == 4:
        print('Quarta-Feira')
    elif s == 5:
        print('Quinta-Feira')
    elif s == 6:
        print('Sexta-Feira')
    elif s == 7:
        print('Sábado')
    else:
        print('Erro! dia da semana inválido')
                            
    n = n + 1
