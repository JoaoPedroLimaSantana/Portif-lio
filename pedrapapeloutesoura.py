import random
lista = ["pedra", "papel", "tesoura"]

resultado_pc = random.choice(lista)
while True:
    sua_decisao = input("pedra, papel ou tesoura? :")
    print("...............................")
    print("o computador escolheu {}".format(resultado_pc))
    if sua_decisao == "tesoura" and resultado_pc == "pedra":
        print("voce perdeu")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "tesoura" and resultado_pc == "papel":
        print("voce ganhou")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "tesoura" and resultado_pc == "tesoura":
        print("deu empate")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "papel" and resultado_pc == "tesoura":
        print("voce perdeu")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "papel" and resultado_pc == "pedra":
        print("voce ganhou")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "papel" and resultado_pc == "papel":
        print("deu empate")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "pedra" and resultado_pc == "papel":
        print("voce perdeu")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "pedra" and resultado_pc == "tesoura":
        print("voce ganhou")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break
    if sua_decisao == "pedra" and resultado_pc == "pedra":
        print("deu empate")
        continuar = input("deseja jogar de novo?(s/n)")
        if continuar == "s":
            continue
        else:
            break



