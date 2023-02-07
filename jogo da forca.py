import random
print('Joguinho da palavra secreta ou forca, digite uma letra\n'
      ' a dica é: almoço.')
lista = ['feijoada','arroz','carne','salada','macarrão']
palavra = random.choice(lista)
letras_acertadas = ''
numerodetentativas = 0
while True:
      numerodetentativas += 1
      letra = input('digite uma letra')
      if len(letra) >1:
            print('digite apenas uma letra')
            continue

      if letra in palavra:
            letras_acertadas += letra
      palavraformada = ''
      for letra in palavra:
            if letra in letras_acertadas:
                  palavraformada += letra
            else:
                  palavraformada += '*'
      print(palavraformada)
      print(numerodetentativas)
      if palavra == palavraformada:
            print('voce acertou')
            break
      print('você tentou {} vezes'.format(numerodetentativas))


