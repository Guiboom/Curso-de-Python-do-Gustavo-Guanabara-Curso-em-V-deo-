números = [[],[],[]]
for i in range(3):
    for j in range(3):
        núm = int(input(f'Digite um número para adicionar à [{i},{j}]: '))
        números[i].append(núm)

soma_pares=0
soma3col=0

for i in números:
    for v in i:
        if v % 2 == 0:
            soma_pares+=v

for linha in números:
    soma3col += linha[2]

maior2lin = números[1][0]
for v in números[1]:
    if v > maior2lin:
        maior2lin = v

# Respostas

print('=-='*15)

for i in números:
    for j in i:
        print(f'[{j:^5}]', end='')
    print()

print('=-='*15)

print(f'A soma de todos os valores pares é: {soma_pares}')
print(f'A soma de todos os valores da 3ª coluna é: {soma3col}')
print(f'O maior valor da segunda linha é: {maior2lin}')