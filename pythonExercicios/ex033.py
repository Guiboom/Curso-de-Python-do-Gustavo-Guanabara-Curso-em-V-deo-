num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
#Verifica qual é monor

if num1 >=num2 and num1>=num3:
    print(f'O numero {num1} é o maior')
elif num2 >=num1 and num2>=num3:
    print(f'O numero {num2} é o maior')
else:
    print(f'O numero {num3} é o maior')

if num1 <=num2 and num1<=num3:
    print(f'O numero {num1} é o menor')
elif num2 <=num1 and num2<=num3:
    print(f'O numero {num2} é o menor')
else:
    print(f'O numero {num3} é o menor')