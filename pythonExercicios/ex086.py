números = [[],[],[]]
for i in range(3):
    for j in range(3):
        núm = int(input(f'Digite um número para adicionar à [{i,j}]: '))
        números[i].append(núm)

for i in números:
    for j in i:
        print(f'[{j:^5}]', end='')
    print()
