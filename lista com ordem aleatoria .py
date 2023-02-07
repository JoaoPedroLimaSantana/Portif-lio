import random
n1 = input('digite o nome do primeiro aluno')
n2 = input('digite o nome do segundo alino')
n3 = input('digite o nome do terceiro aluno')
n4 = input('digite o nome do quarto aluno')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem dos alunos que vão apresentar vai ser {}'.format(lista))

