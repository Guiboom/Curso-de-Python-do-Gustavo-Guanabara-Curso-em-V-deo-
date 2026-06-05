import time

def pyHelp():
    text01= 'SISTEMA DE AJUDA PyHELP'
    print('~'*(len(text01)+4))
    print(' ',text01,' ')
    print('~'*(len(text01)+4))

    while True:
        try:
            chc = input('Função ou Biblioteca: ')
            if chc.upper() == 'FIM':
                print('~'*12)
                print(' ','ATÉ LOGO',' ')
                print('~'*12)
                break
            print('~'*(len(chc)+36))
            print(' ',f'Acessando o manual do comando "{chc}"',' ')
            print('~'*(len(chc)+36))
            time.sleep(2)
            help(chc)
        except:
            print('Digite uma Função ou Biblioteca válida!!!')
            time.sleep(1)
        
pyHelp()