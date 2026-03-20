import random
chute = int(input('Tente adivinhar um número de 0-5: '))
#random=0
num = random.randint(0,5)
if chute == num :
    print('Parabens, você acertou o chute!')
else:
    print(f'Você errou o chute :( o valor era {num}')
