nome = input('digite seu nome')
ndl = len(nome)
if ndl <=4:
    print('seu nome é muito curto')
elif 5 <= ndl <=6:
    print('seu nome é normal')
elif ndl > 6:
    print('seu nome é muito grande')
