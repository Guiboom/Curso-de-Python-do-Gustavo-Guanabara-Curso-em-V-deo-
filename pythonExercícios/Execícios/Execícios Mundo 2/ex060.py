num = int(input('Digite um número: '))
resultado=num
print(f'O fatorial de {num}:')
while num!=0:

    #serve para colocar o 'x' entre cada um
    if num>1:
        print(num,end='x')
    else: 
        print(num,end=' ')
    num = num-1

    #serve para não multiplicar por 0
    if num>1:
        resultado= resultado*(num)

print(f'\nResultado: {resultado}')
