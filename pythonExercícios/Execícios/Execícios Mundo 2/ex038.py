num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
if num1>num2:
    print(f'O número {num1} é o maior.')
elif num2>num1:
    print(f'O número {num2} é o maior.')
else:
    print(f'Não existe valor maior, os dois são iguais')