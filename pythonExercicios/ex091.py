import random
from operator import itemgetter

jogadores = dict()

for j in range(4):
    jogadores[f'jogador{j+1}'] = random.randint(1,6)

print("-"*30)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')

print("-"*30)

jogadores_ordenados = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(jogadores_ordenados):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')