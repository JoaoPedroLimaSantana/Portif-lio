print('lista de compras.')
introducao = input('adicione um item a sua lista, qual item deseja inserir?')
lista = []

enumerate(lista)
lista.append(introducao)
for item in enumerate(lista):
    print(item)
while True:
    comando1 = input('deseja adicionar ou remover um item? responda com "adicionar" ou "remover"')
    if comando1 == 'adicionar':
        mais_item = input('o que deseja adicionar?')
        lista.append(mais_item)
        for item in enumerate(lista):
            print(item)
        continue
    if comando1 == 'remover':
        comando2 = input('digite o numero da lista que deseja remover:')
        comando2_inteiro = int(comando2)
        lista.pop(comando2_inteiro)
        for item in enumerate(lista):
            print(item)
        continue
    else:
        print('digite "adicionar" ou "remover"')
        continue
