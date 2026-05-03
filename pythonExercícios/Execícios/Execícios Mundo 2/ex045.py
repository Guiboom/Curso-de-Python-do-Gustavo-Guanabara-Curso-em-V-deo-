import random
escolha = int(input(
    'Vamos jogar Jokempô:\n'
    '(1)Para pedra\n'
    '(2)Para papel\n'           
    '(3)Para tesoura\n'
    'Digite a sua opção: '           
))
oponente = random.randint(1,3)
if escolha == oponente:
    print('Empate!')
elif escolha == 1 and oponente == 3 or escolha == 2 and oponente == 1 or escolha == 3 and oponente == 2:
    if oponente == 3:
        print('Você Ganhou da tesoura!')
    elif oponente == 2:
        print('Você Ganhou da papel!')
    else:
        print('Você Ganhou da pedra!')
elif escolha>0 and escolha<4:
    if oponente == 3:
        print('Você perdeu para tesoura!')
    elif oponente == 2:
        print('Você perdeu para o papel!')
    else:
        print('Você perdeu para a pedra!')
else:
    print('Digite uma opção valida!')