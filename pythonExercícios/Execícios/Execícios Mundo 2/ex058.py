import random


numR = random.randint(0,10)#número aleatório de 0-10
numC=-1 #numero chute
numC=int(input('Tente acertar um número aleatório de 0-10: '))
tentarivas=1
while numC!=numR:
    if numC < numR:
        resposta='Mais...'
        numC=int(input(f'{resposta} número de 0-10: '))
    elif numC > numR:
        resposta='Menos...'
        numC=int(input(f'{resposta} número de 0-10: '))
    tentarivas+=1
print(f'Parabens, você acertou depois de {tentarivas} tentativas e o número era o {numR}!')
