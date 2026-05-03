#Crie um programa que leia um numero real qualquer pelo teclado e mostra na tela a sua porção inteira
#ex 6.127 será 6
import math
num = float(input('Digite um numero: '))
num2 = math.trunc(num)
print(f'O numero {num} em sua porção inteira é: {num2}')