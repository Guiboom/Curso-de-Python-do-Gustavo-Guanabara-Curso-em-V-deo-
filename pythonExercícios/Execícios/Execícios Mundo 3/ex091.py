import random
from operator import itemgetter

jogadores = dict()

for i in range(4):
    jogadores[f"jogador{+i+1}"] = random.randint(1, 6)

print("-" * 30)

for nomes, numero in jogadores.items():
    print(f"O {nomes} tirou {numero}")

print("-" * 30)

jogadores_ordenados = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

for colocado, (nomes, numero) in enumerate(jogadores_ordenados.items()):
    print(f"{colocado+1}° lugar: {nomes} com {numero}")

print("-" * 30)
