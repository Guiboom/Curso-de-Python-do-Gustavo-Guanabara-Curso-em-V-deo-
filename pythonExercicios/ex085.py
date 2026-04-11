pares_ímpares = [[], []] # [0] é pares, [1] é ímpares

for _ in range(7):

    num = int(input('Digite um número: '))

    if num % 2 == 0:
        pares_ímpares[0].append(num)

    else:
        pares_ímpares[1].append(num)

print("=-="*15)

print(f'Os valores pares digitados foram: {sorted(pares_ímpares[0])}')
print(f'Os valores ímpares digitados foram: {sorted(pares_ímpares[1])}')
