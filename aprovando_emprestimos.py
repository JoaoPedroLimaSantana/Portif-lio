valor_da_casa = int(input("qual o valor da casa? :"))
qnts_anos = int(input("quantos anos você vai pagar? :"))
salario = int(input("qual o seu salario"))#o valor do emprestimo não pode passar de 30% do salario

porcentagem_salario = (salario/100) * 30
calc = (valor_da_casa/qnts_anos)/12
if porcentagem_salario >= calc:
    print("O valor das prestações ficou em {}, seu emprestimo foi aprovado".format(calc))
else:
    print("o valor das prestações ficou em {}, ultrapassando de 30% do seu salario. Seu emprestimo foi negado".format(calc))


