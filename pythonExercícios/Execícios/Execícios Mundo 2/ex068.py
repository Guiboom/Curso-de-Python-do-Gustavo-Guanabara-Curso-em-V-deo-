import random 
text='PAR OU IMPAR'
cont=0

print('=-='*15)
print(f'{text:^45}')
print('=-='*15)

while True:
    n = int(input('Digite um número: '))
    print('---'*15)
    chc = input('Par ou Ímpar? (P/I): ')
    chc = chc.upper()

    if chc != 'I' and chc != 'P':
        print('Escolha invalida!')
        break 

    nb = random.randint(0,11)
    soma = n+nb

    print(f'Você jogou {n} e o computador {nb}')

    print('---'*15)
    if chc == 'P' and soma % 2 == 0 or chc == 'I' and soma % 2 != 0:
        print('Você ganhou!')
        cont+=1
    else:
        print('Você perdeu')
        print('---'*15)
        break
    print('---'*15)

print(f'GAME OVER! Você teve {cont} vitórias consecutivas.')