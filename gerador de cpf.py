import random
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
cpf = nove_digitos
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
dez_digitos = nove_digitos + str(resto_da_divisão_por_onze)
# validar o ultimo numero
contaa0 = 11 * (int(dez_digitos[0]))
contaa1 = 10 * (int(dez_digitos[1]))
contaa2 = 9 * (int(dez_digitos[2]))
contaa3 = 8 * (int(dez_digitos[3]))
contaa4 = 7 * (int(dez_digitos[4]))
contaa5 = 6 * (int(dez_digitos[5]))
contaa6 = 5 * (int(dez_digitos[6]))
contaa7 = 4 * (int(dez_digitos[7]))
contaa8 = 3 * (int(dez_digitos[8]))
contaa9 = 2 * (int(dez_digitos[9]))
total2 = contaa0 + contaa1 + contaa2 + contaa3 + contaa4 + contaa5 + contaa6 + contaa7 + contaa8 + contaa9
multiplicar_por_dez2 = total2 * 10
resto_da_divisão_por_onze2 = multiplicar_por_dez2 % 11
onze_digitos = dez_digitos + str(resto_da_divisão_por_onze2)
print('cpf gerado:{}'.format(onze_digitos))
