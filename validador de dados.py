while True:
    sexo = input("informe seu sexo [M/F]: ")
    if sexo == "":
        print("dados invalidos, por favor informe seu sexo[M/F]")
        continue
    while sexo not in "MmFf":
        sexo = input("dados invalidos, por favor informe seu sexo[M/F]")
    print("sexo cadastrado")