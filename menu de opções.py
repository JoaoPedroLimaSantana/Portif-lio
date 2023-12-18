while True:
    valor1 = int(input("..............................................\ndigite um número: "))
    valor2 = int(input("digite outro número: "))
    opcao = int(input("...............................................\n"
                      "[1] somar\n"
                      "[2] multiplicar\n"
                      "[3] maior\n"
                      "[4] novos números\n"
                      "[5] sair do programa"))
    if opcao == 1:
        soma = int(valor1 + valor2)
        print("A soma de {} mais {} é: {}".format(valor1, valor2, soma))
        continue
    if opcao == 2:
        mult = valor1 * valor2
        print("A multiplicação de {} vezes {} é: {}".format(valor1, valor2, mult))
        continue
    if opcao == 3:
        maior1p2 = bool(valor1 > valor2)
        maior2p1 = bool(valor1 < valor2)
        igual = bool(valor1 == valor2)
        if maior1p2 == True:
            print("{} é maior que {}".format(valor1, valor2))
            continue


        if maior2p1 == True:
            print("{} é maior que {}".format(valor2, valor1))
            continue

        if igual == True:
            print("{} e {} são iguais".format(valor1, valor2))
            continue

    if opcao == 4:
        continue

    if opcao == 5:
        print("voce saiu")
        break





