barras = "="*30
print(barras)
print('{:^30}'.format('BANCO'))
print(barras)
valor = int(input("que valor você quer sabcar R$ "))
total = valor
ced = 200
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print("total de {} cédulas de R$ {}".format(totalced, ced))
        if ced == 200:
            ced == 100
        elif ced == 100:
            ced == 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced == 1
        if total == 0:
            break