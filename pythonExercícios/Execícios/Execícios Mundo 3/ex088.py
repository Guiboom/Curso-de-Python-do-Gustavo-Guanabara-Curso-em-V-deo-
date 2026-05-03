import random
palpites = list()

print("-"*40)
print('MEGA SENA'.center(40))
print("-"*40)

quant = int(input("Quantos jogos você quer que eu sorteie?: "))

print(f"SORTEANDO {quant} JOGOS".center(40,"="))

for i in range(quant):
    palpites.append(sorted(random.sample(range(1,61), 6)))
    print(f"JOGO {i+1}: {palpites[i]}")

print('BOA SORTE'.center(40,"="))