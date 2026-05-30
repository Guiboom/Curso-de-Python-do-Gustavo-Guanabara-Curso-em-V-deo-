import sys
def leiaInt():
    try:
        global n
        n = int(input(f'{n}'))
        
        return(n)
    except:
        #print('ERRO! Digite um número inteiro válido.')
        #sys.exit()
        print()
        
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')