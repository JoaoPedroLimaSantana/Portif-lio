horario = input('que horas são?')

try:
    hora = int(horario)
    if hora > 24:
        print('digite um horario do relogio')
    elif 6 <= hora <= 12:
        print('bom dia')
    elif 13 <= hora <= 18:
        print('boa tarde')
    elif 19 <= hora <= 24:
        print('boa noite')
    elif 1 <= hora <= 5:
        print('você deveria estar dormindo')
    else:
        print('digite um horario')
except:
    print('digite um numero do relogio')

