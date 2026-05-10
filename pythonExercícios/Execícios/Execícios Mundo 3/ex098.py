import time

def contador(inicio,fim,passo):
    passo = abs(passo)
    num = inicio

    if passo == 0:
        passo = 1

    if inicio<fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while num <= fim:
            print(num,end=' ',flush=True)
            num+=passo
            time.sleep(0.5)
        print('FIM')

    if inicio>fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while num >= fim:
            print(num,end=' ',flush=True)
            num-=passo
            time.sleep(0.5)
        print('FIM')

    if inicio==fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while num >= fim-passo:
            print(num,end=' ',flush=True)
            num-=passo
            time.sleep(0.5)
        print('FIM')
            
#contador(1,10,1)
#contador(10,0,2)

print('Agora é com você!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)