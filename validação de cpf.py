cpf = input('digite o cpf')
cpf_em_lista = list(cpf)

conta1 = 10 * (int(cpf_em_lista[0]))
conta2 = 9 * (int(cpf_em_lista[1]))
conta3 = 8 * (int(cpf_em_lista[2]))
conta4 = 7 * (int(cpf_em_lista[3]))
conta5 = 6 * (int(cpf_em_lista[4]))
conta6 = 5 * (int(cpf_em_lista[5]))
conta7 = 4 * (int(cpf_em_lista[6]))
conta8 = 3 * (int(cpf_em_lista[7]))
conta9 = 2 * (int(cpf_em_lista[8]))


total = conta1 + conta2 + conta3 + conta4 + conta5 + conta6 + conta7 + conta8 + conta9
multiplicar_por_dez = total * 10
resto_da_divisão_por_onze = multiplicar_por_dez % 11

if resto_da_divisão_por_onze > 9:
    resto_da_divisão_por_onze == '0'




# validar o ultimo numero
contaa0 = 11 * (int(cpf_em_lista[0]))
contaa1 = 10 * (int(cpf_em_lista[1]))
contaa2 = 9 * (int(cpf_em_lista[2]))
contaa3 = 8 * (int(cpf_em_lista[3]))
contaa4 = 7 * (int(cpf_em_lista[4]))
contaa5 = 6 * (int(cpf_em_lista[5]))
contaa6 = 5 * (int(cpf_em_lista[6]))
contaa7 = 4 * (int(cpf_em_lista[7]))
contaa8 = 3 * (int(cpf_em_lista[8]))
contaa9 = 2 * (int(cpf_em_lista[9]))
total2 = contaa0 + contaa1 + contaa2 + contaa3 + contaa4 + contaa5 + contaa6 + contaa7 + contaa8 + contaa9

multiplicar_por_dez2 = total2 * 10

resto_da_divisão_por_onze2 = multiplicar_por_dez2 % 11


if resto_da_divisão_por_onze2 > 9:
    resto_da_divisão_por_onze2 == '0'


if resto_da_divisão_por_onze == int(cpf_em_lista[9]) and resto_da_divisão_por_onze2 == int(cpf_em_lista[10]):
    print('seu cpf é válido')
else:
    print('seu cpf não é válido')



