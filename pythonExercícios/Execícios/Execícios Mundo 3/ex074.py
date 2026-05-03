# Importa o módulo random e cria uma tupla
from random import randint

num = (
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
    (randint(1, 10)),
)

# Mostra os valores de 4 formas
print("Os valores sorteados foram: ", end="")
for n in num:
    print(f"{n} ", end="")
print(f"\nEm ordem: {sorted(num)}")
print(f"Maior:{max(num)}")
print(f"Menor:{min(num)}")
