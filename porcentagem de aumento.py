sal = float(input('digite seu salario'))
porcentagem_de_aumento = int(input('digite a porcentagem'))
pc = float((sal/100)*porcentagem_de_aumento)
aum = float(sal+pc)
print('seu salario atual é R${}, com o aumento de 15% fica R${}'.format(sal,porcentagem_de_aumento,aum))