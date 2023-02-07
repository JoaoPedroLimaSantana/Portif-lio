print('Ola jogador, para jogar digite as opções escritas entre"". Exemplo: "sim" "não".\n'
      'quando o jogador digita errado o jogo reinicia do 0')
reino = input(' qual sera o nome do reino?')
barras = 150*'_'
opc = 'digite uma opção válida'
nome = input('olá, qual vai ser o seu nome?')
caminho = input('"Finalmente você acordou! Já falei que o senhor bebe até cair. Deseja um copo com... acho que é água." '
                'deseja aceitar a água? "sim" "nao"')
print(barras)
if caminho == 'sim':
    print('você bebeu a "agua"')
    print('mas a agua era tão suja que você acabou morrendo... mais sorte da proxima vez {}. FIM DE JOGO'.format(nome))
elif caminho == 'nao':
    print('você viu que a água estava mais preta que a noite e recusou, o atendente do bar respeita sua decisão e diz\n'
          ' "acho que nao é algo que pode ser bebido"')
    caminho1p2 = input('você acordou em um bar com poucas lembranças da noite anterior. Deseja levantar? "sim" "nao"')
    print(barras)
    if caminho1p2 == 'sim':
        print('você se levanta e vai até a porta onde um batalhão da cavalaria real anuncia\n'
        '"estamos a procura de {}, vamos procura-lo em cada casa e estabelecimento do reino"'.format(nome))
        caminho1p3 = input('se entregar?"sim" "nao"')
        print(barras)
        if caminho1p3 == 'sim':
            print('um cavaleiro com armadura prateada com detalhes dourados desce do seu cavalo,\n'
             'olha no fundo dos seus olhos e diz "você deve ser {}, venha comigo imediatamente'.format(nome))
            caminho1p4 = input('ir com o cavaleiro?"sim" "nao"')
            print(barras)
            if caminho1p4 == "sim" or "não":
                print('você vai com o cavaleiro querendo ou não já que ele literalmente te pega no colo')
                cavalgada = input('você junto ao cavaleiro seguem em direção ao castelo real, porém, seu lado homoafetivo não para de reparar nos glúteos avantajados\n'
                'do cavaleiro, por algum motivo apenas os glúteos estão desprotegidos. você pensa em dar uma apalpadinha.\n'
                'dar uma apalpadinha? "sim" "nao"')
                print(barras)
                if cavalgada == 'sim':
                    print('o cavaleiro se irrita e deixa você cair de propósito\n'
                          'você acaba batendo a cabeça no chão e e os cavalos que estavam atras acabam te pisoteando. Você morreu. FIM DE JOGO (para de ser gay)')
                elif cavalgada == 'não':
                    print('você segura suas vontades intimas e segue para o castelo (o cavaleiro notou você encarando seus glùteos)')
                    print('ROTA HEROI')
            else :
                print(opc)
        elif caminho1p3 == 'nao':
            print('você finge que nao sabe de nada e vai embora. Para evitar mais cavaleiros você pega um atalho\n'
             'por um beco que leva a sua casa, no caminho você é abordado por um ladrão.')
            ladrao = input('"dar tudo" ou "revidar"')
            print(barras)
            if ladrao == 'dar tudo':
                print('o ladão rouba tudo de você e te apunhala. Você morreu. FIM DE JOGO')
            elif ladrao == 'revidar':
                print('o ladrão fica com medo da suas incríveis habilidades de luta e vai embora.\n'
                'Na realidade ele ficou com pena, você esta todo acabado e sujo e ainda fica fazendo movimentos estranhos')
                print('no caminho de casa alguém te reconhece\n'
                '"{}! EU ESTAVA TE PROCURANDO POR TODO CANTO! O REINO TODO ESTA TE PROCURANDO E NINGUÉM SABE O MOTIVO"'.format(nome))
                print('você pede para essa pessoa se acalmar e se revelar, afinal ela está toda de preto e com o rosto coberto por uma mascara')
                print('È revelador que a pessoa misteriosa é Fernandinho, seu parceiro de copo.\n'
                      'Fernandinho diz "{} vá para a fazenda da minha familia, la ninguém chega perto, cuide da fazenda e ela cuidará de você"'.format(nome))
                fazenda = input('ir para a fazenda?"sim" "nao')
                print(barras)
                if fazenda == 'sim':
                    print('você arruma suas coisas e vai para a fazenda da familia do Fernandinho')
                    print('ROTA FAZENDINHA FELIZ')
                elif fazenda == 'nao':
                    print('você agradece o Fernandinho mas recusa a oferta, você esta despreocupado\n'
                    ' e nao liga se os cavaleiros querem a sua cabeça ou nao')
                    print('você segue para casa e alguns mercenarios te acham e um te noceuteia achando que você é alguém de valor, já que os cavaleiros\n'
                    'do rei estão a sua procura')
                    mercenarios = input('você acorda em uma sala escura rodeado de homens armados, um pergunta "quem é você e por que estão te procurando?"\n'
                    'mas você também não sabe o motivo. O que você faz? "mentir" ou "verdade"')
                    print(barras)
                    if mercenarios == 'mentir':
                        print('você mente falando que é o filho perdido do rei e que tem muito valor')
                        print('o mercenario abre um sorriso de orelha a orelha e diz "então quer me dizer que você é alguém importante?\n'
                        'Ouviram rapazes? O bonito aqui é importante, quanto que a cabeça dele deve valer?"')
                        print('você responde que vale muito e que vale mais ainda se não estiver machucado')
                        print('o mercenario diz "tenho uma ideia melhor, não vou te devolver para o seu papai, vou te vender no mercado negro de outro pais,\n'
                              'la você deve valer muito mais, imagine "o filho perdido do rei de {} sendo vendido como escravo."'. format(reino))
                        escravo = input('você claramente não quer ser escravo (eu acho). chorar" por misericordia ou "lutar"')
                        if escravo == 'chorar':
                            print('não adiantou nada, você foi contrabandeado para um pais vizinho e vendido como escravo para um homem que gosta\n'
                            'de se relacionar com seus escravos')
                            print('FINAL ESCRAVO SEXUAL')
                            print('você não morreu mas virou uma putinha')
                            print('FIM DE JOGO')
                        elif escravo == 'lutar':
                            print('você tentou se soltar mas passou vergonha e os mercenarios te mataram')
                            print('FIM DE JOGO')
                        else :
                            print(opc)
                    elif mercenarios == 'verdade'
                        print('o mercenario não vê valor em você e apenas te mata')
                        print('FIM DE JOGO')
                    else :
                        print(opc)

                else :
                    print(opc)

            else :
                print(opc)
        else :
            print(opc)
    elif caminho1p2 == 'nao':
        print('você volta a dormir mas é acordado com cavaleiros anunciando\n'
              "estamos a procura de {},vamos procura-lo em cada casa e estabelecimento do reino" 'você cai e machuca a perna'.format(nome))
        caminhosla = input('se entregar?"sim" "nao"')
        print(barras)
        if caminhosla == 'sim':
            print('um cavaleiro com armadura prateada com detalhes dourados desce do seu cavalo,\n'
             'olha no fundo dos seus olhos e diz "você deve ser {}, venha comigo imediatamente'.format(nome))
            caminho1p4 = input('ir com o cavaleiro?"sim" "nao"')
            print(barras)
            if caminho1p4 == "sim" or "não":
                print('você vai com o cavaleiro querendo ou não já que ele literalmente te pega no colo')
                cavalgada = input('você junto ao cavaleiro seguem em direção ao castelo real, porém, seu lado homoafetivo não para de reparar nos glúteos avantajados\n'
                'do cavaleiro, por algum motivo apenas os glúteos estão desprotegidos. você pensa em dar uma apalpadinha.\n'
                'dar uma apalpadinha? "sim" "nao"')
                print(barras)
                if cavalgada == 'sim':
                    print('o cavaleiro se irrita e deixa você cair de propósito\n'
                          'você acaba batendo a cabeça no chão e e os cavalos que estavam atras acabam te pisoteando. Você morreu. FIM DE JOGO (para de ser gay)')
                elif cavalgada == 'não':
                    print('você segura suas vontades intimas e segue para o castelo (o cavaleiro notou você encarando seus glùteos)')
                    print('ROTA HEROI')
                else :
                    print(opc)

        elif caminho == 'nao':
            print('você finge que nao sabe de nada e vai embora. Para evitar mais cavaleiros você pega um atalho\n'
             'por um beco que leva a sua casa, no caminho você é abordado por um ladrão.')
            ladrao = input('"dar tudo" ou "revidar"')
            print(barras)
            if ladrao == "dar tudo":
                print('o ladão rouba tudo de você e te apunhala. Você morreu. FIM DE JOGO')
            elif ladrao == 'revidar':
                print('você tenta revidar mas sua perna falhou durante o combate. O ladrão te apunhalou.\n'
                 'Você morreu. FIM DE JOGO')
            else :
                print(opc)
        else :
            print(opc)

    else :
        print(opc)

else :
    print(opc)



