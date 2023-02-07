while True:
    print('calculadora maluca')
    n1 = (input('digite o primeiro numero'))
    opr = input('digite a operação adição"+" subtração"-" multiplicação"x" divisão"% ou /"')
    n2 = (input('digite o segundo numero'))
    nval = None
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        nval = True
    except:
        nval = None
    if nval == None:
        print('digite um numero valido')
    oprval = '+-/%x'
    if opr not in oprval:
        print('digite um operador valido')
        continue
    if len(opr) > 1:
        print('digite apenas um operador')
        continue












    if opr == '+':
        print(n1 + n2)
    if opr == '-':
        print(n1-n2)
    if opr == 'x':
        print(n1*n2)
    if opr == '%':
        print(n1/n2)
    if opr == '/':
        print(n1/n2)

