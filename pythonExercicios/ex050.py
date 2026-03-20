s=0
for c in range(0,6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s+=num
print(f'A soma de todos os números pares digitados são:{s}')
