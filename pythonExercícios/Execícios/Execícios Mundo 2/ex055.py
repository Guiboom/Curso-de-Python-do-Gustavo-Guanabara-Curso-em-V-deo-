maior=0
menor=0
for c in range(5):
    pesoP = float(input('Digite o peso da pessoa em kg: '))
    if c == 0:
        maior = pesoP
        menor = pesoP
    else:
        if pesoP > maior:
            maior = pesoP
        if pesoP < menor:
            menor = pesoP
print(f'O maior desses peso é: {maior}Kg, e o menor é {menor}Kg')
    